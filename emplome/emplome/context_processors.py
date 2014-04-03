from django.contrib.sites.models import Site
from django.db import models
from web.models import *

def site_variables(request):
    current_site = Site.objects.get_current()
    ctx_location = []
    ctx_function = []
    jobs = Job.objects.all()
    for job in jobs:
        ctx_location.append(job.job_location)
    for job in jobs:
        ctx_function.append(job.function)

    return {
        'SITE_ROOT_URL_S': 'http://%s/'%(current_site.domain),
        'SITE_ROOT_URL': 'http://%s'%(current_site.domain),
        'locations': ctx_location,
        'functions': ctx_function,
    }