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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        print function
        skills = request.GET.get('skills', '')
        exp = request.GET.get('experience', '')
        industry = request.GET.get('industry', '')
        search_flag = request.GET.get('search', '')
        if search_flag == 'true':
            search = True
        jobs = []
        if location and function and skills and exp and not search:
            experience = int(exp)

            jobs = Job.objects.filter(Q(job_location__icontains=location) , Q(function=function), Q(skills__icontains=skills), Q(exp_req_min__lte=experience, exp_req_max__gte=experience), is_publish=True).order_by('-id').order_by('order')

            if not jobs.exists():
                searched_for = str('"'+location+ '-'+skills+'-'+function+'-'+exp+'"')
        
        elif location and not function and not skills and not exp and not industry and not search: 
            jobs = Job.objects.filter(job_location__icontains=location, is_publish=True).order_by('-id').order_by('order')    
            if not jobs.exists():
                searched_for = str('"'+location+'"')       
        elif function and not location and not skills and not exp and not industry and not search:
            jobs = Job.objects.filter(function=function, is_publish=True).order_by('-id').order_by('order')
            if not jobs.exists():
                searched_for = str('"'+function+'"')
        elif skills and not location and not function and not exp and not industry and not search:
            jobs = Job.objects.filter(skills__icontains=skills, is_publish=True).order_by('-id').order_by('order')

            if not jobs.exists():
                searched_for = str('"'+skills+'"')   
        else:
            if location == 'undefined':
                location = ''
            if function == 'undefined':
                function = ''
            if skills == 'undefined':
                skills = ''
            if industry == 'undefined':
                industry = ''
            if len(exp) > 0 and exp != 'undefined': 
                jobs = Job.objects.filter(job_location__contains=location, function__contains=function, skills__icontains=skills, exp_req_min__lte=int(exp), exp_req_max__gte=int(exp), is_publish=True).order_by('-id').order_by('order')
            elif exp == 'undefined' or exp == '':
                jobs = Job.objects.filter(job_location__icontains=location, function__contains=function , skills__icontains=skills, industry__contains=industry, is_publish=True).order_by('-id').order_by('order')
                
            if not jobs.exists():
                searched_for = ''
        context = {
            'jobs': jobs,
        }
        searched_for = ''

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
        next_url = request.GET.get('next', '')
        context = {
            'next': next_url,
        }
        return render(request, 'login_job_seeker.html', context)    

    def post(self, request, *args, **kwargs):
        context = {}
        
        if len(request.POST['email']) > 0 and not request.POST['email'].isspace() and len(request.POST['password']) > 0 \
        and not request.POST['password'].isspace():
            
            user = authenticate(username=request.POST['email'], password=request.POST['password'])
            
            if user and user.is_active:
                if user.is_superuser and user.userprofile_set.all().count() == 0:
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
                'message' : 'Username or Password cannot be null',
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
        companyprofile.description = post_dict['description']
        recruiter, created = RecruiterProfile.objects.get_or_create(profile=userprofile)
        recruiter.company = companyprofile

        recruiter.save()
        if created:
            login_user = authenticate(username=post_dict['email'], password=post_dict['password'])
            if login_user and login_user.is_active:
                login(request, login_user)
        else:
            if request.is_ajax():
                res = {
                    'message': 'User already exists',
                    'result': 'error',
                }
                response = simplejson.dumps(res)
                status_code = 500
                return HttpResponse(response, status = status_code, mimetype='application/json')
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
        try:
            if request.user.is_authenticated():
                user = request.user
                user_created = False
            else:
                user, user_created = User.objects.get_or_create(username=seeker['email'])
                if not user_created:
                    if request.is_ajax():
                        res = {
                            'message': 'User already exists',
                            'result': 'error',
                        }
                        response = simplejson.dumps(res)
                        status_code = 500
                        return HttpResponse(response, status = status_code, mimetype='application/json')
            if user.email != seeker['email']:
                user.username = seeker['email']
            user.email=seeker['email']
            user.first_name=seeker['first_name']
            if user_created:
                user.set_password(seeker['password'])
            user.save()
        except IntegrityError, ex:
            status_code = 500
            response = simplejson.dumps({
                'result': 'error', 
                'message': 'This email already existing'
            })
            return HttpResponse(response, status = status_code, mimetype = 'application/json')
        
        userprofile, created = UserProfile.objects.get_or_create(user = user)
        
        userprofile.user_type = 'job_seeker'
        userprofile.country = seeker['country']
        userprofile.city = seeker['city']
        userprofile.mobile = seeker['mobile']
        userprofile.save()

        job_seeker, job_seeker_created = JobSeekerProfile.objects.get_or_create(profile = userprofile)

        job_seeker.gender = seeker['gender']
        job_seeker.religion = seeker['religion']
        job_seeker.dob = datetime.strptime(seeker['dob'], '%d-%m-%Y')
        current_year = dt.datetime.now().year        
        age = current_year - job_seeker.dob.year

        job_seeker.age = age
        job_seeker.marital_status = seeker['marital_status']
        job_seeker.nationality = seeker['nationality']
        
        if seeker['alt_email'] != "":
            job_seeker.alt_mail = seeker['alt_email']
        job_seeker.save()
        
        if job_seeker_created:
            education = Education()
            employment = Employment()
        else:
            education = job_seeker.education if job_seeker.education else Education()
            employment = job_seeker.employment if job_seeker.employment else Employment()
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
        education.save()
        job_seeker.education = education
        job_seeker.employment = employment
        job_seeker.save()
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
        jobseeker, created = JobSeekerProfile.objects.get_or_create(profile = userprofile)
        seeker1 = ast.literal_eval(post_data['seeker1'])
        if jobseeker.employment:
            employment = jobseeker.employment
        else:
            employment = Employment()
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
        jobseeker.employment = employment
        jobseeker.save()
        photo = request.FILES.get('photo_img', '')
        if photo:
            jobseeker.photo = photo
        jobseeker.save()
        education = jobseeker.education
        certificate = request.FILES.get('certificate_img', '')
        if certificate:
            education.certificate = certificate
        education.save()
        jobseeker.education = education
        jobseeker.save()
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

        jobPosting = Job.objects.create(recruiter = current_user)
        post_data = request.POST
        print post_data
        jobpost = ast.literal_eval(post_data['jobpost'])
        
        profile = current_user.userprofile_set.all()[0]
        company, created = CompanyProfile.objects.get_or_create(company_name = jobpost['company'])
        jobPosting.job_title = jobpost['title']
        jobPosting.ref_code = jobpost['code']
        jobPosting.company = company
        jobPosting.summary = jobpost['summary']
        document = request.FILES.get('product_pdf', '')
        if document:
            jobPosting.document = document
        jobPosting.salary =jobpost['salary']
        jobPosting.currency =jobpost['currency']    
        jobPosting.skills =jobpost['skills']
        jobPosting.industry = jobpost['industry']
        jobPosting.job_location = jobpost['location']
        jobPosting.education_req = jobpost['requirement']
        jobPosting.function = jobpost['function']
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
        jobs = Job.objects.filter(recruiter=request.user)
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
        company, created = CompanyProfile.objects.get_or_create(company_name = jobpost['company'])
        jobPosting.company = company
        jobPosting.summary = jobpost['summary']

        document = request.FILES.get('product_pdf', '')
        if document:
            jobPosting.document = document
        jobPosting.salary =jobpost['salary']
        jobPosting.currency =jobpost['currency'] 
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
            print jobPosting.last_date
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


class JobDetailsView(View):
    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id=kwargs['job_id'])
        
        context = {
           'job' : job, 
        }
        if request.is_ajax():
            ctx_jobpost = []
                   
            ctx_jobpost.append({
                'title': job.job_title if job.job_title else '',
                'code': job.ref_code if job.ref_code else '',
                'company': job.company.company_name if job.company else '',
                'summary': job.summary if job.summary else '',            
                'details': job.document.name if job.document else '',             
                'skills': job.skills if job.skills else '',
                'min':job.exp_req_min if job.exp_req_min else '',
                'max':job.exp_req_max if job.exp_req_max else '',
                'location':job.job_location if job.job_location else '',
                'industry':job.industry if job.industry else '',
                'function': job.function if job.function else '',            
                'requirement': job.education_req if job.education_req else '',
                'specialisation': job.specialization if job.specialization else '',
                'nationality': job.nationality if job.nationality else '',
                'last_date': job.last_date.strftime('%d-%m-%Y') if job.last_date else '',
                'name': job.name if job.name else '',
                'phone': job.phone if job.phone else '',
                'email': job.mail_id if job.mail_id else '',
                'profile':job.description if job.description else '', 
                'post_date': job.posting_date.strftime('%d-%m-%Y') if job.posting_date else '', 
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
        jobseeker = []
        company = []
        if user.userprofile_set.all().count() > 0:
            userprofile = user.userprofile_set.all()[0]
            if userprofile.user_type == 'job_seeker':
                if userprofile.jobseekerprofile_set.all().count() >0:
                    jobseeker = userprofile.jobseekerprofile_set.all()[0]

                ctx_seeker.append ({
                    'email': user.email,
                    'first_name': user.first_name,
                    'gender': jobseeker.gender if jobseeker else '',
                    'dob': jobseeker.dob.strftime('%d-%m-%Y') if jobseeker else '',
                    'religion': jobseeker.religion if jobseeker else '',
                    'marital_status': jobseeker.marital_status if jobseeker else '',
                    'nationality': jobseeker.nationality if jobseeker else '',
                    'country': userprofile.country if userprofile else '',
                    'city': userprofile.city if userprofile else '',
                    'mobile': userprofile.mobile if userprofile else '',
                    'alt_email': jobseeker.alt_mail if jobseeker else '',
                    'basic_edu': jobseeker.education.basic_edu if jobseeker.education else '' ,
                    'pass_year_basic': jobseeker.education.pass_year_basic if jobseeker.education else '' ,
                    'masters_edu': jobseeker.education.masters if jobseeker.education else '' ,
                    'pass_year_masters': jobseeker.education.pass_year_masters if jobseeker.education else '' ,
                    'doctrate': jobseeker.education.doctrate if jobseeker.education else '' ,
                    'resume_title': jobseeker.education.resume_title if jobseeker.education else '' ,
                    'resume_text': jobseeker.education.resume_text if jobseeker.education else '' ,
                    'resume': jobseeker.education.resume.name if jobseeker.education else '' ,
                })

                ctx_seeker1.append({
                    'years': jobseeker.employment.exp_yrs if jobseeker.employment else '' ,
                    'months': jobseeker.employment.exp_mnths if jobseeker.employment else '' ,
                    'salary': jobseeker.employment.salary if jobseeker.employment else '' ,
                    'designation': jobseeker.employment.designation if jobseeker.employment else '' ,
                    'skills': jobseeker.employment.skills if jobseeker.employment else '' ,
                    'industry': jobseeker.employment.curr_industry if jobseeker.employment else '' ,
                    'functions': jobseeker.employment.function if jobseeker.employment else '' , 
                    'certificate_img': jobseeker.education.certificate.name if jobseeker.education else '',
                    'profile_photo': jobseeker.photo.name if jobseeker else '',
                })
            else:
                if userprofile.recruiterprofile_set.all().count() > 0:
                    recruiter = userprofile.recruiterprofile_set.all()[0]
                    
                    company = recruiter.company

                ctx_recruiter.append({
                    'name' : company.company_name if company else '' ,
                    'industry' : company.industry_type if company else '' ,
                    'email' : user.email,
                    'country' : userprofile.country if userprofile else '',
                    'mobile' : userprofile.mobile if userprofile else '',
                    'phone' : userprofile.land_num if userprofile else '',
                    'city': userprofile.city if userprofile else '',
                    'description': company.description if company else '',
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
            try:
                site_url = Site.objects.get_current().domain
            except:
                site_url = Site.objects.all()[0]
            url = 'http://%s%s'%(site_url,'/reset_password/'+str(user.id)+'/') 
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
                    msg.send()
                    context = {
                        'message': 'An email has been sent to your registered email address. Please click on the link provided in the mail to reset your password.',
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
            recruiter, created = RecruiterProfile.objects.get_or_create(profile = userprofile)
            company = recruiter.company
            company.company_name = post_dict['name']
            company.industry_type = post_dict['industry']
            company.description = post_dict['description']
            company.save()
            recruiter.company = company
            recruiter.save()
            
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
            
            status_code = 500

        response = simplejson.dumps(res)

        return HttpResponse(response, status = status_code, mimetype="application/json")


class SuccessStoriesView(View):

    def get(self, request, *args, **kwargs):

        success_stories = SuccessStory.objects.all()
        paginator = Paginator(success_stories, 3)
        page = request.GET.get('page')
        try:
            stories = paginator.page(page)
        except PageNotAnInteger:
            stories = paginator.page(1)
        except EmptyPage:
            stories = paginator.page(paginator.num_pages)
        context = {
            'success_stories': stories,
        }
        return render(request, 'success_stories.html', context)


class PublishJob(View):

    def get(self, request, *args, **kwargs):

        try:
            job = Job.objects.get(id = kwargs['job_id'])
            job.is_publish = True
            job.save()
            jobs = Job.objects.filter(recruiter=request.user)
        except Exception as ex:
            print str(ex)
            jobs = []
        context = {
          'jobs': jobs,
          'message': 'Published', 
        }

        return HttpResponseRedirect(reverse('posted_jobs'))


class DeleteJob(View):

    def get(self, request, *args, **kwargs):

        try:
            job = Job.objects.get(id = kwargs['job_id'])
            job.delete()
            jobs = Job.objects.filter(recruiter=request.user)
        except Exception as ex:
            print str(ex)
            jobs = []
        context = {
          'jobs': jobs,
          'message': 'Deleted',
        }
        return HttpResponseRedirect(reverse('posted_jobs'))


class SearchCV(View):

    def get(self, request, *args, **kwargs):

        search = False
        cv_title = request.GET.get('cv_title', '')
        age = request.GET.get('age', '')
        keyword = request.GET.get('keyword', '')
        jobseeker_profiles = []

        if cv_title == 'undefined':
            cv_title = ''
        if keyword == 'undefined':
            keyword = ''

        if len(age) > 0 and age != 'undefined': 
            jobseeker_profiles = JobSeekerProfile.objects.filter(education__resume_title__icontains= cv_title, age = age, employment__skills__icontains=keyword).distinct('id')

        elif age == 'undefined' :
            jobseeker_profiles = JobSeekerProfile.objects.filter(education__resume_title__icontains= cv_title, employment__skills__icontains=keyword).distinct('id')
        
        context = {
            'cvs': jobseeker_profiles,
        }
              
        return render(request, 'search_cvs_result.html', context) 


class Companies(View):

    def get(self, request, *args, **kwargs):

        ctx_companies = []
        companies = CompanyProfile.objects.all()
        if companies.count() > 0:
            for company in companies:
                ctx_companies.append({
                    'name': company.company_name,
                })
        res = {
            'companies': ctx_companies,
            
        } 
        response = simplejson.dumps(res)
        status_code = 200
        return HttpResponse(response, status=status_code, mimetype="application/json")


class ApplyJobs(View):

    def get(self, request, *args, **kwargs):

        current_user = request.user
        current_date = dt.datetime.now().date()
        context = {}
        job = Job.objects.get(id = kwargs['job_id'])

        if current_user.userprofile_set.all().count > 0:
            if current_user.userprofile_set.all()[0].user_type == 'job_seeker':
                jobseeker, created = JobSeekerProfile.objects.get_or_create(profile__user = current_user)
                if job.last_date:
                    if job.last_date < current_date:
                        context = {
                            'message' : 'Time expired, you cannot apply',
                            'job' : job,
                        }
                        return render(request, 'job_details.html', context)

                jobseeker.applied_jobs.add(job)
                jobseeker.save()
            else:
                context = {
                    'message': 'You cannot apply',
                    'job' : job,
                }
                return render(request, 'job_details.html', context)

        context = {
            'job' : job,
        }

        return render(request, 'job_details.html', context)


class AppliedJobsView(View):

    def get(self, request, *args, **kwargs):

        applied_jobs = []
        profile = UserProfile.objects.get(user_id = kwargs['user_id'])
        jobseeker_profile = profile.jobseekerprofile_set.all()[0]
        applied_jobs = jobseeker_profile.applied_jobs.all()
        context = {
            'applied_jobs':applied_jobs,
        }
        
        return render(request, 'applied_jobs.html', context)
  

class FeaturedJobView(View):

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id = kwargs['job_id'])
        context = {
            'job': job,
        }
        return render(request, 'job_details.html', context)


class AppliedUsers(View):

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id=kwargs['job_id'])
        profiles = job.jobseekerprofile_set.all()
        context = {
            'job': job,
            'profiles': profiles,
        }
        return render(request, 'applied_users.html', context)





