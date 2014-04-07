from django.contrib.sites.models import Site
from django.db import models
from web.models import *

def site_variables(request):
    current_site = Site.objects.get_current()
    ctx_location = []
    ctx_function = []
    jobs = Job.objects.all()
    for job in jobs:
        if job.job_location not in ctx_location:
            ctx_location.append(job.job_location)
    for job in jobs:
        if job.function not in ctx_function:
            ctx_function.append(job.function)
    try:
        success_stories = SuccessStory.objects.all().exclude(publish=False)
        print success_stories
    except:
        success_stories = []


    return {
        'SITE_ROOT_URL_S': 'http://%s/'%(current_site.domain),
        'SITE_ROOT_URL': 'http://%s'%(current_site.domain),
        'locations': ctx_location,
        'functions': ctx_function,
        'success_stories': success_stories,
    }