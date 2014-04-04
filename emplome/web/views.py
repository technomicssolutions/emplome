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
        employer = True
        context = {
            'employer': employer,
        }
        return render(request, 'recruiter_home.html', {})

class FullTime(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'full_time.html', context)

class RecruiterRegistrationView(View):

    def get(self, request, *args, **kwargs):

        logout(request)
        
        return render(request, 'recruiter_registration.html', {})

    def post(self, request, *args, **kwargs):
        post_dict = request.POST
        user, created = User.objects.get_or_create(username=request.POST['email'])
        user.email = request.POST['email']
        user.set_password(post_dict['password'])
        user.save()
        userprofile = UserProfile()
        userprofile.user = user
        userprofile.user_type = "employer"
        userprofile.mobile=request.POST['mobile']
        userprofile.land_num=request.POST['phone']
        userprofile.city=request.POST['city']
        userprofile.country=request.POST['country']
        userprofile.save()
        companyprofile = CompanyProfile() 
        companyprofile.company_name = request.POST['name']
        companyprofile.industry_type = request.POST['industry']
        companyprofile.save()
        userprofile.company = companyprofile
        userprofile.save()
        login_user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if login_user and login_user.is_active:
            login(request, login_user)

        context = {
            'profile': userprofile,
        }
        return render(request, 'profile.html', context)

    
class JobSeekerRegistration(View):

    def get(self, request,*args, **kwargs):
        
        logout(request)
        return render(request, 'job_seeker_registration.html', {})

    def post(self, request, *args, **kwargs):

        post_data = request.POST
        seeker = ast.literal_eval(post_data['seeker'])
        user, created = User.objects.get_or_create(username=seeker['email'], email=seeker['email'],first_name=seeker['first_name'])
        user.set_password(seeker['password'])
        user.save()
        
        userprofile = UserProfile()
        # userprofile, created = UserProfile.objects.get_or_create(userprofile=userprofile)
        userprofile.user = user
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
        
        # education = Education()
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
        # if seeker['resume_doc'] != "null":
        #   education.resume = request.FILES['resume_doc']
        if seeker['resume_text'] != "":
            education.resume_text = seeker['resume_text']
        education.userprofile = userprofile
        education.save()
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

        jobPosting = Job()
        post_data = request.POST
        jobpost = ast.literal_eval(post_data['jobpost'])
        current_user = request.user
        profile = current_user.userprofile_set.all()[0]
        jobs = profile.applied_jobs.all()
        
        jobPosting.user = current_user
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
    def post(self, request, *args, **kwargs):

        jobPosting =Job.objects.get(id= kwargs['user_id'])
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


class ListExistingJobs(View):
    def get(self, request,*args, **kwargs):
        ctx_jobs = []
        current_user = request.user
        profile = UserProfile.objects.get(user = current_user)
        # company = CompanyProfile.objects.get(user = profile)
        jobs = profile.applied_jobs.all()
        if request.is_ajax():
            if len(jobs) > 0:
                for job in jobs:
                    ctx_jobs.append({
                        'ref_code': job.ref_code
                    })
            res = {
                'existing_jobs': ctx_jobs,
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
        job = JobPosting.objects.filter(ref_code = kwargs['ref_code'],company_name = company)
        if request.is_ajax():
            ctx_jobs.append({
                'title':job[0].job_title,
                'summary': job[0].summary,
                'details': job[0].job_details,
                'skills': job[0].skills,
                'location':job[0].job_location,
                'industry':job[0].industry,
                'function': job[0].function,
                'role':job[0].role,
                'requirement': job[0].education_req,
                'specialisation':job[0].specialization,
                'nationality': job[0].nationality,
                'min':job[0].exp_req_min,
                'max':job[0].exp_req_max,
                'profile':job[0].company_profile,

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

        return render(request, 'job_details.html', context)

class SearchView(View):

    def get(self, request, *args, **kwargs):
         context = {}

         return render(request, 'search.html', context)
       
