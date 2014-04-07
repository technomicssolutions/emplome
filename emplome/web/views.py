# Create your views here.
import datetime as dt
from datetime import datetime

import simplejson
import ast

from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.db import IntegrityError
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError, EmailMessage, EmailMultiAlternatives, mail_admins
from django.contrib.sites.models import Site
from django.template.loader import render_to_string

from django.http import Http404 

from web.models import *


class Home(View):
    def get(self, request, *args, **kwargs):
        
        context = {}
        
        return render(request, 'home.html', context)

class SearchJobsView(View):

    def get(self, request, *args, **kwargs):

        search = False
        location = request.GET.get('location', '')
        function = request.GET.get('function', '')
        skills = request.GET.get('skills', '')
        exp = request.GET.get('experience', '')
        industry = request.GET.get('industry', '')
        search_flag = request.GET.get('search', '')
        if search_flag == 'true':
            search = True
        jobs = []
        if location and function and skills and exp and not search:
            experience = int(exp)
            jobs = Job.objects.filter(Q(job_location=location) , Q(function=function), Q(skills=skills), Q(exp_req_min__lte=experience, exp_req_max__gte=experience))
            if not jobs.exists():
                searched_for = str('"'+location+ '-'+skills+'-'+function+'-'+exp+'"')
        
        elif location and not function and not skills and not exp and not industry and not search: 
            jobs = Job.objects.filter(job_location=location)    
            if not jobs.exists():
                searched_for = str('"'+location+'"')       
        elif function and not location and not skills and not exp and not industry and not search:
            jobs = Job.objects.filter(function=function)
            if not jobs.exists():
                searched_for = str('"'+function+'"')
        elif skills and not location and not function and not exp and not industry and not search:
            jobs = Job.objects.filter(skills__contains=skills)
            if not jobs.exists():
                searched_for = str('"'+skills+'"')   
        else:
            if exp:
                jobs = Job.objects.filter(Q(job_location__contains=location) | Q(function__contains=function) | Q(skills__contains=skills)| Q(industry__contains=industry))
            else:
                jobs = Job.objects.filter(Q(job_location__contains=location) | Q(function__contains=function) | Q(skills__contains=skills)| Q(industry__contains=industry) | Q(exp_req_min__gte=int(exp), exp_req_max__lte=int(exp)))
            if not jobs.exists():
                searched_for = ''
                # exp_req_min__gte=exp, exp_req_max__lte=exp,

        
        context = {
            'jobs': jobs,
        }

        if len(jobs) == 0:
            context.update({
                'searched_for': searched_for,
            })
        
        return render(request, 'search_jobs.html', context) 

        

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('home'))
        

class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'login_job_seeker.html', context)    

    def post(self, request, *args, **kwargs):
        context = {}
        if len(request.POST['email']) > 0 and not request.POST['email'].isspace() and len(request.POST['password']) > 0 \
        and not request.POST['password'].isspace():
            
            user = authenticate(username=request.POST['email'], password=request.POST['password'])
            
            if user and user.is_active:
                if user.is_superuser:
                    context = {
                        'message': 'You have no profile',
                    }
                    return render(request, 'recruiter_home.html', context)
                userdata = UserProfile.objects.get(user = user)
                login(request, user)
            else:
                context = {
                    'message' : 'Username or Password is incorrect',
                }
                context.update(request.POST)
                if request.POST['user_type'] == 'recruiter':
                    return render(request, 'recruiter_home.html', context)
                else:
                    return render(request, 'login_job_seeker.html', context)
            if userdata.user_type == 'employer':
                return HttpResponseRedirect(reverse('profile',args=[user.id]))
            else:
                return HttpResponseRedirect(reverse('profile',args=[user.id]))
        else:
            context = {
                'message' : 'Username and Password cannot be null',
            }
            context.update(request.POST)
            if request.POST['user_type'] == 'recruiter':
                return render(request, 'recruiter_home.html', context)
            else:
                return render(request, 'login_job_seeker.html', context)

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        try:
            user = User.objects.get(id = kwargs['user_id'])
            profile = UserProfile.objects.get(user = user)
            context = {
                'profile': profile,
            }
        except:
            context = {
                'error':'You have no profile'
        }
        return render(request, 'profile.html', context) 

class RecruiterHomeView(View):
    def get(self, request, *args, **kwargs):
        
        logout(request)
        employer = True
        context = {
            'employer': employer,
        }
        return render(request, 'recruiter_home.html', {})

class RecruiterRegistrationView(View):

    def get(self, request, *args, **kwargs):

        context = {
            'user_loggedin': False,
            'user_id': '',
        }
        return render(request, 'recruiter_registration.html', context)

    def post(self, request, *args, **kwargs):

        
        post_dict = ast.literal_eval(request.POST['recruiter'])
        
        user, created = User.objects.get_or_create(username=post_dict['email'])
        user.email = post_dict['email']
        if created:
            user.set_password(post_dict['password'])
        user.save()
        userprofile, created = UserProfile.objects.get_or_create(user = user)
        userprofile.user_type = "employer"
        userprofile.mobile = post_dict['mobile']
        userprofile.land_num = post_dict['phone']
        userprofile.city = post_dict['city']
        userprofile.country = post_dict['country']
        userprofile.save()
        companyprofile, created = CompanyProfile.objects.get_or_create(company_name = post_dict['name'], industry_type = post_dict['industry']) 
        
        userprofile.company = companyprofile
        userprofile.save()
        if created:
            login_user = authenticate(username=post_dict['email'], password=post_dict['password'])
            if login_user and login_user.is_active:
                login(request, login_user)
        if request.is_ajax():
            res = {
                'user_id': user.id,
                'result': 'ok',
            }
            response = simplejson.dumps(res)
            status_code = 200
            return HttpResponse(response, status = status_code, mimetype='application/json')
        else:
            context = {
                'profile': userprofile,
            }
            return render(request, 'profile.html', context)

    
class JobSeekerRegistration(View):

    def get(self, request,*args, **kwargs):
        
        return render(request, 'job_seeker_registration.html', {})

    def post(self, request, *args, **kwargs):

        post_data = request.POST
        seeker = ast.literal_eval(post_data['seeker'])
        user, user_created = User.objects.get_or_create(username=seeker['email'], email=seeker['email'],first_name=seeker['first_name'])
        if user_created:
            user.set_password(seeker['password'])
        user.save()
        
        userprofile, created = UserProfile.objects.get_or_create(user = user)
        
        userprofile.user_type = 'job_seeker'
        userprofile.gender = seeker['gender']
        userprofile.religion = seeker['religion']
        userprofile.marital_status = seeker['marital_status']
        userprofile.nationality = seeker['nationality']
        userprofile.country = seeker['country']
        userprofile.city = seeker['city']
        userprofile.mobile = int(seeker['mobile'])
        if seeker['alt_email'] != "":
            userprofile.alt_mail = seeker['alt_email']
        userprofile.save()
        
        education, created = Education.objects.get_or_create(userprofile=userprofile)
        education.basic_edu = seeker['basic_edu']
        education.pass_year_basic = int(seeker['pass_year_basic'])
        if seeker['masters_edu'] != "":
            education.masters = seeker['masters_edu']
        if seeker['pass_year_masters'] != "":
            education.pass_year_masters = int(seeker['pass_year_masters'])
        if seeker['doctrate'] != "":
            education.doctrate = seeker['doctrate']
        education.resume_title = seeker['resume_title']

        resume = request.FILES.get('resume_doc', '')
        if resume:
            education.resume = resume
       
        if seeker['resume_text'] != "":
            education.resume_text = seeker['resume_text']
        education.userprofile = userprofile
        education.save()
        if user_created:
            login_user = authenticate(username=seeker['email'], password=seeker['password'])
            if login_user and login_user.is_active:
                login(request, login_user)
        res = {
            'result': 'ok',
            'user_id': user.id,
        }
        response = simplejson.dumps(res)
        status_code = 200
        return HttpResponse(response, status=status_code, mimetype='application/json')



        
class JobSeekerRegistrationMoreInfo(View):
    def get(self, request,*args, **kwargs):
        context = {
            'is_profile_edit': True,
            'user_id' : kwargs['user_id'],
        }

        return render(request, 'job_seeker_registration_more_info.html', context)

    def post(self, request, *args, **kwargs):
        post_data = request.POST
        userprofile = UserProfile.objects.get(user_id=kwargs['user_id'])
        seeker1 = ast.literal_eval(post_data['seeker1'])
        employment, created = Employment.objects.get_or_create(userprofile=userprofile)
        employment.exp_yrs = int(seeker1['years'])
        if seeker1['months'] != "":
            employment.exp_mnths = int(seeker1['months'])
        if seeker1['salary'] != "":
            employment.salary = int(seeker1['salary'])
        if seeker1['designation'] != "":
            employment.designation = seeker1['designation']
        if seeker1['industry'] != "":
            employment.curr_industry = seeker1['industry']
        if seeker1['functions'] != "":
            
            employment.function = seeker1['functions']
        employment.skills = seeker1['skills']
        employment.save()
        photo = request.FILES.get('photo_img', '')
        if photo:
            userprofile.photo = photo
        userprofile.save()
        education, created = Education.objects.get_or_create(userprofile=userprofile)
        certificate = request.FILES.get('certificate_img', '')
        if certificate:
            education.certificate = certificate
        education.save()

        res = {
            'result': 'ok',
            'user_id': kwargs['user_id'],
        }
        response = simplejson.dumps(res)
        status_code = 200
        return HttpResponse(response, status=status_code, mimetype='application/json')

class PostJobsView(View):
    def get(self, request,*args, **kwargs):
        context = {
        }
        return render(request, 'job_post.html', context)

    def post(self, request, *args, **kwargs):

        current_user = request.user

        jobPosting, created = Job.objects.get_or_create(user = current_user)
        post_data = request.POST
        jobpost = ast.literal_eval(post_data['jobpost'])
        
        profile = current_user.userprofile_set.all()[0]
        
        jobPosting.company = profile.company
        jobPosting.job_title = jobpost['title']
        jobPosting.ref_code = jobpost['code']
        jobPosting.summary = jobpost['summary']
        document = request.FILES.get('product_pdf', '')
        if document:
            jobPosting.document = document
        jobPosting.skills =jobpost['skills']
        jobPosting.industry = jobpost['industry']
        jobPosting.job_location = jobpost['location']
        jobPosting.function = jobpost['function']
        jobPosting.education_req = jobpost['requirement']
        jobPosting.specialization = jobpost['specialisation']
        jobPosting.nationality = jobpost['nationality']
        if jobpost['last_date']:
            jobPosting.last_date  = datetime.strptime(jobpost['last_date'], '%d-%m-%Y')
        jobPosting.name = jobpost['name']
        jobPosting.phone = jobpost['phone']
        jobPosting.mail_id = jobpost['email']
        jobPosting.description = jobpost['profile']
        if jobpost['post_date']:
            jobPosting.posting_date = datetime.strptime(jobpost['post_date'], '%d-%m-%Y')
        jobPosting.exp_req_min = jobpost['min']
        jobPosting.exp_req_max = jobpost['max']
        jobPosting.save()

        res = {
            'id' : jobPosting.id,
            'message':'data posted on our server'
        } 
        response = simplejson.dumps(res)
        status_code = 200
        return HttpResponse(response, status = status_code, mimetype="application/json")



class PostedJobsView(View):
     def get(self, request,*args, **kwargs):
        jobs = []
        jobs = Job.objects.filter(user=request.user)
        context = {
          'jobs': jobs,
        }
        return render(request, 'posted_jobs.html', context)



class EditPostJobsView(View):

    def get(self, request, *args, **kwargs):
        job_id = kwargs['job_id']

        context = {
            'job_id':job_id,
        }
        return render(request, 'job_post.html', context)

    def post(self, request, *args, **kwargs):

        jobPosting =Job.objects.get(id= kwargs['job_id'])
        post_data = request.POST

        jobpost = ast.literal_eval(post_data['jobpost'])
        jobPosting.job_title = jobpost['title']
        jobPosting.ref_code = jobpost['code']
        jobPosting.summary = jobpost['summary']

        document = request.FILES.get('product_pdf', '')
        if document:
            jobPosting.document = document
        jobPosting.skills =jobpost['skills']
        jobPosting.industry = jobpost['industry']
        jobPosting.job_location = jobpost['location']
        jobPosting.function = jobpost['function']
        jobPosting.education_req = jobpost['requirement']
        jobPosting.specialization = jobpost['specialisation']
        jobPosting.nationality = jobpost['nationality']
        jobPosting.name = jobpost['name']
        jobPosting.phone = jobpost['phone']
        jobPosting.mail_id = jobpost['email']
        jobPosting.description = jobpost['profile']        
        jobPosting.exp_req_min = jobpost['min']
        jobPosting.exp_req_max = jobpost['max']

        if jobpost['last_date']:
            jobPosting.last_date  = datetime.strptime(jobpost['last_date'], '%d-%m-%Y')
        if jobpost['post_date']:
            jobPosting.posting_date = datetime.strptime(jobpost['post_date'], '%d-%m-%Y')
        jobPosting.save()
        context = {}
        res = {
            'id' : jobPosting.id,
        } 
        response = simplejson.dumps(res)
        status_code = 200
        return HttpResponse(response, status = status_code, mimetype="application/json")


class ListExistingJobDetails(View):
    def get(self, request,*args, **kwargs):
        ctx_jobs = []
        current_user = request.user
        profile = UserProfile.objects.get(user = current_user)
        company = CompanyProfile.objects.get(user = profile)
        job = Job.objects.filter(ref_code = kwargs['ref_code'],company_name = company)
        if request.is_ajax():
            ctx_jobs.append({
                'title': job[0].job_title,
                'code': job[0].ref_code,
                'summary': job[0].summary,            
                'details': job[0].document.name,            
                'skills': job[0].skills,
                'min':job[0].exp_req_min,
                'max':job[0].exp_req_max,
                'location':job[0].job_location,
                'industry':job[0].industry,
                'function': job[0].function,            
                'requirement': job[0].education_req,
                'specialisation': job[0].specialization,
                'nationality': job[0].nationality,
                'last_date': job[0].last_date,
                'name': job[0].name,
                'phone': job[0].phone,
                'email': job[0].mail_id,
                'profile':job[0].description, 
                'post_date': job[0].posting_date, 
            })
            res = {
                'existing_job_details': ctx_jobs,
            }
        response = simplejson.dumps(res)
        status_code = 200
        return HttpResponse(response, status = status_code, mimetype="application/json")

class JobDetailsView(View):
    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id=kwargs['job_id'])
        
        context = {
           'job' : job, 
        }
        if request.is_ajax():
            ctx_jobpost = []
                   
            ctx_jobpost.append({
                'title': job.job_title,
                'code': job.ref_code,
                'summary': job.summary,            
                'details': job.document.name,            
                'skills': job.skills,
                'min':job.exp_req_min,
                'max':job.exp_req_max,
                'location':job.job_location,
                'industry':job.industry,
                'function': job.function,            
                'requirement': job.education_req,
                'specialisation': job.specialization,
                'nationality': job.nationality,
                'last_date': job.last_date,
                'name': job.name,
                'phone': job.phone,
                'email': job.mail_id,
                'profile':job.description, 
                'post_date': job.posting_date, 
            })
            
            res = {
                'jobpost': ctx_jobpost,
            }
            status_code = 200
            response = simplejson.dumps(res)
            
            return HttpResponse(response, status=status_code, mimetype='application/json')
        else:
            return render(request, 'job_details.html', context)

class SearchView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        location = request.GET.get('location', '')
        skills = request.GET.get('skills', '')
        function = request.GET.get('function', '')
        industry = request.GET.get('industry', '')
        if location:
            context = {
                'location': True,
            }          

        elif skills:
            context = {
                'skills': True,
            }        

        elif function:
            context = {
                'function': True,
            }        

        elif industry:
            context = {
                'industry': True,
            }

        return render(request, 'search.html', context) 

    
class EditProfile(View):

    def get(self, request, *args, **kwargs):

        user_id = kwargs['user_id']
        context = {
            'is_profile_edit': True,
            'user_id': user_id,
        }
        return render(request, 'job_seeker_registration.html', context)

class GetProfileDetails(View):

    def get(self, request, *args, **kwargs):

        user_id = kwargs['user_id']
        user = User.objects.get(id= user_id)
        ctx_seeker = []
        ctx_seeker1 = []
        ctx_recruiter = []
        education = []
        employment = []
        company = []
        if user.userprofile_set.all().count() > 0:
            userprofile = user.userprofile_set.all()[0]
            if userprofile.user_type == 'job_seeker':
                if userprofile.education_set.all().count() > 0:
                    education = userprofile.education_set.all()[0]
                
                if userprofile.employment_set.all().count() > 0:
                    employment = userprofile.employment_set.all()[0]
                ctx_seeker.append({
                    'email': user.email,
                    'first_name': user.first_name,
                    'gender': userprofile.gender if userprofile else '',
                    'religion': userprofile.religion if userprofile else '',
                    'marital_status': userprofile.marital_status if userprofile else '',
                    'nationality': userprofile.nationality if userprofile else '',
                    'country': userprofile.country if userprofile else '',
                    'city': userprofile.city if userprofile else '',
                    'mobile': userprofile.mobile if userprofile else '',
                    'alt_email': userprofile.alt_mail if userprofile else '',
                    'basic_edu': education.basic_edu if education else '' ,
                    'pass_year_basic': education.pass_year_basic if education else '' ,
                    'masters_edu': education.masters if education else '' ,
                    'pass_year_masters': education.pass_year_masters if education else '' ,
                    'doctrate': education.doctrate if education else '' ,
                    'resume_title': education.resume_title if education else '' ,
                    'resume_text': education.resume_text if education else '' ,
                    'resume': education.resume.name if education else '' ,
                })
                ctx_seeker1.append({
                    'years': employment.exp_yrs if employment else '' ,
                    'months': employment.exp_mnths if employment else '' ,
                    'salary': employment.salary if employment else '' ,
                    'designation': employment.designation if employment else '' ,
                    'skills': employment.skills if employment else '' ,
                    'industry': employment.curr_industry if employment else '' ,
                    'functions': employment.function if employment else '' , 
                    'certificate_img': education.certificate.name if education else '',
                    'profile_photo': userprofile.photo.name if userprofile else '',
                })
            else:
                
                company = userprofile.company

                if userprofile.employment_set.all().count() > 0:
                    employment = userprofile.employment_set.all()[0]

                ctx_recruiter.append({
                    'name' : company.company_name if company else '' ,
                    'industry' : company.industry_type if company else '' ,
                    'email' : user.email,
                    'country' : userprofile.country if userprofile else '',
                    'mobile' : userprofile.mobile if userprofile else '',
                    'phone' : userprofile.land_num if userprofile else '',
                    'city': userprofile.city if userprofile else '',
                })
        if request.is_ajax():
            res = {
                'seeker': ctx_seeker,
                'seeker1': ctx_seeker1,
                'recruiter': ctx_recruiter,
                'result': 'ok',
            }
            status_code = 200

            response = simplejson.dumps(res)
            
            return HttpResponse(response, status=status_code, mimetype='application/json')

class ForgotPassword(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'forgot_password.html', {})

    def post(self, request, *args, **kwargs):

        user = User.objects.filter(email = request.POST['email_id'])
        if user.exists():
            user = user[0]
            subject = 'Reset Your Password'
            text_content = 'This is Important'
            from_email = settings.DEFAULT_FROM_EMAIL
            url = 'http://%s%s'%(Site.objects.get_current().domain,'/reset_password/'+str(user.id)+'/') 
            ctx = {
                'url': url,
                'user': user,
            }
            html_content = render_to_string('email/forgot_password.html', ctx)
            to = []
            if subject and html_content and from_email:
                
                to.append(user.email)
                for i in range(len(to)):
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to[i]])
                    msg.attach_alternative(html_content, "text/html")
                    try:
                        msg.send()
                        context = {
                            'message': 'An email has been sent to your registered email address. Please click on the link provided in the mail to reset your password.',
                        }
                        return render(request, 'forgot_password.html', context)
                    except Exception as ex:
                        context = {
                            'message': 'Please try after some time',
                        }
                        return render(request, 'forgot_password.html', context)

        else:
            context = {
                'message': 'You have no matching profiles with this email id',
            }
            return render(request, 'forgot_password.html', context)

class ResetPassword(View):

    def get(self, request, *args, **kwargs):
        
        user_id = kwargs['user_id']
        context = {
            'user_id': user_id
        }
        return render(request, 'reset_password.html', context)

    def post(self, request, *args, **kwargs):

        user_id = kwargs['user_id']
        user = User.objects.get(id=int(user_id))
        if len(request.POST['new_password']) > 0 and not request.POST['new_password'].isspace():
            user.set_password(request.POST['new_password'])
            user.save()
            context = {
                'success_message': 'Password changed successfully',
                'user_id': user_id
            }
        else:
            context = {
                'message': 'Password should have a minimum length of 6',
                'user_id': user_id,
            }
        return render(request, 'reset_password.html', context)

class RecruiterProfileEdit(View):

    def get(self, request, *args, **kwargs):

        user = User.objects.get(id=kwargs['user_id'])
        context = {
            'user_loggedin': True,
            'user_id': user.id,
        }

        return render(request, 'recruiter_registration.html', context)

    def post(self, request, *args, **kwargs):

        try:
            post_dict = ast.literal_eval(request.POST['recruiter'])
            user = User.objects.get(id=kwargs['user_id'])
            user.email = post_dict['email']
            user.save()
            userprofile, created = UserProfile.objects.get_or_create(user = user)
            userprofile.mobile = post_dict['mobile']
            userprofile.land_num = post_dict['phone']
            userprofile.city = post_dict['city']
            userprofile.country = post_dict['country']
            userprofile.save()
            company = userprofile.company
            company.company_name = post_dict['name']
            company.industry_type = post_dict['industry']
            company.save()
            userprofile.company = company
            userprofile.save()
            
            res = {
                'result':'ok',
                'message': 'successfully edited',
                'user_id': user.id,
            }
            
            status_code = 200
        except Exception as ex:
            res = {
                'result':'error',
                'message': 'successfully edited',
                'error_message': str(ex),
            }
            
            status_code = 200

        response = simplejson.dumps(res)

        return HttpResponse(response, status = status_code, mimetype="application/json")
