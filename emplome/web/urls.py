from django.conf.urls import patterns, include, url

from web.views import *

urlpatterns = patterns('',
	url(r'^$', Home.as_view(), name='home'),
	url(r'^full-time/$', FullTime.as_view(), name='full_time'),
	url(r'^recruiter/$', RecruiterHomeView.as_view(), name='recruiter'),
	url(r'^recruiter-reg/$', RecruiterRegistrationView.as_view(), name='register'),
	url(r'^job_seeker_registration/$', JobSeekerRegistration.as_view(), name='job_seeker_registration'),
)