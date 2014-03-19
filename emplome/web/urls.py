from django.conf.urls import patterns, include, url

from web.views import *

urlpatterns = patterns('',
	url(r'^$', Home.as_view(), name='home'),
	url(r'^job_seeker_registration$', JobSeekerRegistration.as_view(), name='job_seeker_registration'),
	url(r'^full-time/', FullTime.as_view(), name='full_time')


	# url(r'^$', FullTime.as_view(), name='join')
)