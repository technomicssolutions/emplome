# Create your views here.
import datetime
from datetime import timedelta

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

class LoginView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'login_job_seeker.html', context)	

	def post(self, request, *args, **kwargs):
		user = authenticate(username=request.POST['email'], password=request.POST['password'])
		print "user",user
		userdata = UserProfile.objects.get(user = user)
		print "userdata",userdata.user_type
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
		companyprofile.company_name = request.POST['type']
		companyprofile.save()

		context = {}
		return render(request, 'job_post.html', context)

	
class JobSeekerRegistration(View):
	def get(self, request,*args, **kwargs):
		context = {}
		return render(request, 'job_seeker_registration.html', context)

class JobSeekerRegistration2(View):
	def get(self, request,*args, **kwargs):
		context = {}
		return render(request, 'job_seeker_registration_2.html', context)

class EmployerProfileView(View):
	def get(self, request,*args, **kwargs):
		context = {}
		return render(request, 'recruiter_home.html', context)



