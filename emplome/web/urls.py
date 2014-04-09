from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from web.views import *

urlpatterns = patterns('',
	url(r'^$', Home.as_view(), name='home'),
	
	url(r'^accounts/login/$', LoginView.as_view(), name='login'),
	url(r'^logout/$', Logout.as_view(), name='logout'),

	url(r'^recruiter/$', RecruiterHomeView.as_view(), name='recruiter'),
	url(r'^recruiter-registration/$', RecruiterRegistrationView.as_view(), name='register'),
	url(r'^recruiter/post-jobs/$',login_required(PostJobsView.as_view()), name='postjobs'),
	url(r'^recruiter/post-jobs/edit/(?P<job_id>\d+)/$',login_required(EditPostJobsView.as_view()), name='post_jobs_edit'),
	url(r'^job/details/(?P<job_id>\d+)/$',JobDetailsView.as_view(), name='job_details'),
	url(r'^applied_jobs/(?P<user_id>\d+)/$', login_required(AppliedJobsView.as_view()), name='applied_jobs'),

	url(r'^job_seeker_registration/$', JobSeekerRegistration.as_view(), name='job_seeker_registration'),
	url(r'^job_seeker_registration_more_info/(?P<user_id>\d+)/$', JobSeekerRegistrationMoreInfo.as_view(), name='job_seeker_registration_more_info'),
	url(r'^posted_jobs/$', login_required(PostedJobsView.as_view()), name='posted_jobs'),

	url(r'^profile/(?P<user_id>\d+)/$',login_required(ProfileView.as_view()), name='profile'),
	url(r'^edit_profile/(?P<user_id>\d+)/$', login_required(EditProfile.as_view()), name='edit_profile'),
	url(r'^profile/details/(?P<user_id>\d+)/$', GetProfileDetails.as_view(), name='profile_details'),
	url(r'^edit_profile/recruiter/(?P<user_id>\d+)/$', login_required(RecruiterProfileEdit.as_view()), name='edit_profile_recruiter'),

	url(r'^search/jobs/$',SearchJobsView.as_view(), name='search_jobs'),
	url(r'^search/$', SearchView.as_view(), name='search'),

	url(r'^forgot_password/$', ForgotPassword.as_view(), name='forgot_password'),
	url(r'^reset_password/(?P<user_id>\d+)/$', ResetPassword.as_view(), name='reset_password'),

	url(r'^success_stories/$', SuccessStoriesView.as_view(), name='success_stories'),

	url(r'^job/delete/(?P<job_id>\d+)/$', DeleteJob.as_view(), name='delete_job'),
	url(r'^job/publish/(?P<job_id>\d+)/$', PublishJob.as_view(), name='publish_job'),
	url(r'^search_cv/$',SearchCV.as_view(), name='search_cv'),

	url(r'^companies/$', Companies.as_view(), name='companies'),

	url(r'^apply/(?P<job_id>\d+)/$', login_required(ApplyJobs.as_view()), name='apply_jobs'),


)