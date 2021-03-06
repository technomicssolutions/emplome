from django.contrib.sites.models import Site
from django.db import models
from web.models import *

def site_variables(request):
    try:
        current_site = Site.objects.get_current()
    except:
        current_site = Site.objects.all()[0]
    ctx_location = []
    ctx_function = []
    ctx_featured_job = []
    stories = []
    recommendation = []
    jobs = Job.objects.filter(is_publish=True).order_by('-id').order_by('order')
    featured_jobs = Job.objects.filter(is_publish=True, is_featured=True).order_by('-id').order_by('order')
    for job in jobs:
        if job.job_location not in ctx_location:
            ctx_location.append(job.job_location)
    for job in jobs:
        if job.function not in ctx_function:
            ctx_function.append(job.function)
    for job in featured_jobs:
        ctx_featured_job.append(job)
    try:
        success_stories = SuccessStory.objects.filter(publish=True).order_by('-id')
        if success_stories.count() > 3:
            stories = success_stories[:3]
        elif success_stories.count() <= 3:
            stories = success_stories
    except:
        stories = []
    try:
        recommendations = Recommendation.objects.all().order_by('-id')
        if recommendations.count() > 3:
            recommendation = recommendations[:3]
        elif recommendations.count() <= 3:
            recommendation = recommendations
    except:
        recommendation = []
    
    return {
        'SITE_ROOT_URL_S': 'http://%s/'%(current_site.domain),
        'SITE_ROOT_URL': 'http://%s'%(current_site.domain),
        'locations': ctx_location,
        'functions': ctx_function,
        'success_stories': stories ,
        'recommendations': recommendation ,
        'featured_jobs': ctx_featured_job,
    }