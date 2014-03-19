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

class JobSeekerRegistration(View):
	def get(self, request,*args, **kwargs):
		context = {}
		return render(request, 'job_seeker_registration.html', context)

