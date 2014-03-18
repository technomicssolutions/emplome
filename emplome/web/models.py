from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

USER_TYPE = (
	('admin', 'Admin'),
	('employer', 'Employer'),
	('job_seeker', 'Job Seeker'),
)

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	user_type = models.CharField('User Type', max_length=20, choices=USER_TYPE)
	gender = models.CharField('Gender', max_length=1)
	nationality = models.CharField('Nationality', max_length=10)
	current_location = models.CharField('Current Loction', null=True, blank=True, max_length=20)
	country = models.CharField('Country', null=True, blank=True, max_length=20)
	city = models.CharField('City', null=True, blank=True, max_length=20)
	mobile = models.IntegerField ('Mobile')
	land_num = models.IntegerField('Land Phone', blank=True)
	mail_id = models.CharField('Email Id', max_length=25)
	Alt_mail = models.CharField('Alternate Email Id', null=True, blank=True, max_length=25)
	religion = models.CharField('Religion', null=True, blank=True, max_length=10)
	marital_status = models.CharField('Marital Status', null=True, blank=True, max_length=10)

class Employment(models.Model):
	user = models.ForeignKey(UserProfile)
	exp_yrs = land_num = models.IntegerField('Experience in Years', blank=True)
	exp_mnths = models.IntegerField('Experience in Months', blank=True)
	salary = models.IntegerField('Salary', null=True, blank=True)
	designation = models.CharField('Designation', null=True, blank=True, max_length=15)
	industry_type = models.CharField('Industry Type', null=True, blank=True, max_length=20)
	skills = models.CharField('Key Skills', null=True, blank=True, max_length=20)
	curr_industry = models.CharField('Current Industry', null=True, blank=True, max_length=20)

class Education(models.Model):
	user = models.ForeignKey(UserProfile)
	basic_edu = models.CharField('Basic Education', max_length=15)
	basic_spl = models.CharField('Specialisation1', max_length=20)
	masters = models.CharField('Masters', null=True, blank=True, max_length=15)
	master_spl = models.CharField('Specialisation2', null=True, blank=True, max_length=20)
	doctorate = models.CharField('Doctorate', null=True, blank=True, max_length=20)

class CompanyProfile(models.Model):
	user = models.ForeignKey(UserProfile)
	employer_name = models.CharField('Employer Name', max_length=15)
	company_name = models.CharField('Company Name', max_length=20)
	industry_type = models.CharField('Industry Type', max_length=20)
	mobile = models.IntegerField('Mobile')
	land_num = models.IntegerField('Land Phone', null=True, blank=True)
	city = models.CharField('City', null=True, blank=True, max_length=20)
	country = models.CharField('Country', null=True, blank=True, max_length=15)

class JobPosting(models.Model):
	job_type = models.CharField('Job Type', max_length=20)
	posting_date = models.DateTimeField('Posting Date', null=True, blank=True)
	last_date = models.DateTimeField('Last Date', null=True, blank=True)
	exp_req = models.IntegerField('Experience Required', null=True, blank=True)
	skills = models.CharField('Skills Required', null=True, blank=True, max_length=20)

		

# Create your models here.
