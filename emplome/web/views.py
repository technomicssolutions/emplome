# Create your views here.
import datetime
from datetime import timedelta

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

from web.models import *


class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home.html', context)

class Logout(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		return HttpResponseRedirect(reverse('home'))

class LoginView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'login_job_seeker.html', context)	

	def post(self, request, *args, **kwargs):
		user = authenticate(username=request.POST['email'], password=request.POST['password'])
		userdata = UserProfile.objects.get(user = user)
		if user and user.is_active:
			login(request, user)
		else:
			context = {
				'message' : 'Username or password is incorrect',
			}
			return render(request, 'login_job_seeker.html',context)

		if userdata.user_type == 'employer':
			return HttpResponseRedirect(reverse('empprofile',args=[user.id]))
		else:
			return HttpResponseRedirect(reverse('profile',args=[user.id]))

class JobSeekerProfileView(View):
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
		return render(request, 'job_seeker_profile.html', context)	

class RecruiterHomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'recruiter_home.html', {})

class FullTime(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'full_time.html', context)

class RecruiterRegistrationView(View):

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'recruiter_registration.html', context)

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
		companyprofile.user = userprofile
		companyprofile.company_name = request.POST['name']
		companyprofile.industry_type = request.POST['type']
		companyprofile.save()

		context = {}
		return render(request, 'recruiter_profile.html', context)

	
class JobSeekerRegistration(View):
	def get(self, request,*args, **kwargs):
		context = {}
		return render(request, 'job_seeker_registration.html', context)

class JobSeekerRegistration2(View):
	def get(self, request,*args, **kwargs):
		context = {}
		return render(request, 'job_seeker_registration_2.html', context)

class EmployerProfileView(View):
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
		return render(request, 'recruiter_profile.html', context)

class PostJobsView(View):
	def get(self, request,*args, **kwargs):
		context = {
		}
		return render(request, 'job_post.html', context)

	def post(self, request, *args, **kwargs):

		jobPosting =JobPosting()
		post_data = request.POST
		jobpost = ast.literal_eval(post_data['jobpost'])
		current_user = request.user
		profile = UserProfile.objects.get(user = current_user)
		company = CompanyProfile.objects.get(user = profile)
		jobPosting.company_name = company
		jobPosting.job_title = jobpost['title']
		jobPosting.ref_code = jobpost['code']
		jobPosting.summary = jobpost['summary']
		jobPosting.job_details = jobpost['details']
		jobPosting.document = request.FILES['product_pdf']
		jobPosting.skills =jobpost['skills']
		jobPosting.order = 1
		jobPosting.industry = jobpost['industry']
		jobPosting.job_location = jobpost['location']
		jobPosting.function = jobpost['function']
		jobPosting.role = jobpost['role']
		jobPosting.education_req = jobpost['requirement']
		jobPosting.specialization = jobpost['specialisation']
		jobPosting.nationality = jobpost['nationality']
		jobPosting.name = jobpost['name']
		jobPosting.phone = jobpost['phone']
		jobPosting.mail_id = jobpost['email']
		jobPosting.company_profile = jobpost['profile']
		jobPosting.exp_req_min = jobpost['min']
		jobPosting.exp_req_max = jobpost['max']
		jobPosting.save()
		print "jobPosting",jobPosting.id
		res = {
			'id' : jobPosting.id,
		} 
		response = simplejson.dumps(res)
		status_code = 200
		return HttpResponse(response, status = status_code, mimetype="application/json")

class EditPostJobsView(View):
	def post(self, request, *args, **kwargs):
		jobPosting =JobPosting.objects.get(id= kwargs['user_id'])
		print "jobPosting",jobPosting
		post_data = request.POST
		jobpost = ast.literal_eval(post_data['jobpost'])
		jobPosting.job_title = jobpost['title']
		jobPosting.ref_code = jobpost['code']
		jobPosting.summary = jobpost['summary']
		jobPosting.job_details = jobpost['details']
		jobPosting.document = request.FILES['product_pdf']
		jobPosting.skills =jobpost['skills']
		jobPosting.order = 1
		jobPosting.industry = jobpost['industry']
		jobPosting.job_location = jobpost['location']
		jobPosting.function = jobpost['function']
		jobPosting.role = jobpost['role']
		jobPosting.education_req = jobpost['requirement']
		jobPosting.specialization = jobpost['specialisation']
		jobPosting.nationality = jobpost['nationality']
		jobPosting.name = jobpost['name']
		jobPosting.phone = jobpost['phone']
		jobPosting.mail_id = jobpost['email']
		jobPosting.company_profile = jobpost['profile']
		jobPosting.exp_req_min = jobpost['min']
		jobPosting.exp_req_max = jobpost['max']
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
		company = CompanyProfile.objects.get(user = profile)
		jobs = JobPosting.objects.filter(company_name = company)
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
		print "jobs",job
		if request.is_ajax():
			ctx_jobs.append({
				'job_title': job[0].job_title,
				'summarys': job[0].summary,
				'job_details': job[0].job_details,
				'skills': job[0].skills,
				'order': job[0].order,
				'industry': job[0].industry,
				'job_location': job[0].job_location,
				'functions': job[0].function,
				'role': job[0].role,
				'education_req': job[0].education_req,
				'specialization': job[0].specialization,
				'nationality': job[0].nationality,
				'company_profile': job[0].company_profile,
				'exp_req_min': job[0].exp_req_min,
				'exp_req_max': job[0].exp_req_max,
			})
			res = {
				'existing_job_details': ctx_jobs,
			}
		response = simplejson.dumps(res)
		status_code = 200
		return HttpResponse(response, status = status_code, mimetype="application/json")







