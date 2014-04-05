from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from web.views import *

urlpatterns = patterns('',
	url(r'^$', Home.as_view(), name='home'),
	url(r'^full-time/$', FullTime.as_view(), name='full_time'),
	url(r'^recruiter/$', RecruiterHomeView.as_view(), name='recruiter'),
	url(r'^recruiter-registration/$', RecruiterRegistrationView.as_view(), name='register'),
	url(r'^job_seeker_registration/$', JobSeekerRegistration.as_view(), name='job_seeker_registration'),
	url(r'^job_seeker_registration_more_info/(?P<user_id>\d+)/$', JobSeekerRegistrationMoreInfo.as_view(), name='job_seeker_registration_more_info'),
	url(r'^accounts/login/$', LoginView.as_view(), name='login'),
	url(r'^logout/$', Logout.as_view(), name='logout'),
	url(r'^profile/(?P<user_id>\d+)/$',login_required(ProfileView.as_view()), name='profile'),
	url(r'^recruiter/post-jobs/$',login_required(PostJobsView.as_view()), name='postjobs'),
	url(r'^recruiter/post-jobs/edit/(?P<job_id>\d+)/$',login_required(EditPostJobsView.as_view()), name='post_jobs_edit'),
	url(r'^jobs/list/$',ListExistingJobs.as_view(), name='list_jobs'),
	# url(r'^jobs/details/(?P<ref_code>[\w-]+)/$',ListExistingJobDetails.as_view(), name='JobDetails'),
	url(r'^search/jobs/$',SearchJobsView.as_view(), name='search_jobs'),
	url(r'^job/details/(?P<job_id>\d+)/$',JobDetailsView.as_view(), name='job_details'),
	url(r'^search/$', SearchView.as_view(), name='search'),
	url(r'^posted_jobs/$', login_required(PostedJobsView.as_view()), name='posted_jobs'),
	url(r'^edit_profile/(?P<user_id>\d+)/$', login_required(EditProfile.as_view()), name='edit_profile'),
	url(r'^profile/details/(?P<user_id>\d+)/$', GetProfileDetails.as_view(), name='profile_details'),
	
)