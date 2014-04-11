from django.contrib.sites.models import Site
from django.db import models
from web.models import *

def site_variables(request):
    current_site = Site.objects.get_current()
    ctx_location = []
    ctx_function = []
    stories = []
    recommendation = []
    jobs = Job.objects.filter(is_publish=True)
    for job in jobs:
        if job.job_location not in ctx_location:
            ctx_location.append(job.job_location)
    for job in jobs:
        if job.function not in ctx_function:
            ctx_function.append(job.function)
    try:
        success_stories = SuccessStory.objects.filter(publish=True).order_by('-id').order_by('order');
        if success_stories.count() > 3:
            stories = success_stories[:3]
        elif success_stories.count() <= 3:
            stories = success_stories
    except:
        stories = []
    try:
        recommendations = Recommendation.objects.all().order_by('-id').order_by('order');
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
    }