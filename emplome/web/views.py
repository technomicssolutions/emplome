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

class FullTime(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'full_time.html', context)

class RecruiterRegistrationView(View):

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'recruiter_registration.html', context)

	def post(self, request, *args, **kwargs):

		user, created = User.objects.get_or_create(username=request.POST['name'])
		user.save()
		userprofile = UserProfile()
		userprofile.user = user
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

	