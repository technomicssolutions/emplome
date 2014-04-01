from django.contrib.sites.models import Site
from django.db import models
from web.models import *

def site_variables(request):
    current_site = Site.objects.get_current()
    ctx_location = []
    ctx_category = []
    jobs = Job.objects.all()
    for job in jobs:
        ctx_location.append(job.job_location)
        
    # for category in categories:
    #     ctx_category.append(job.category)
  
    # header_objs = Homepage.objects.all()
    # if ( header_objs ):
    #     header_obj = header_objs[0]
    # else:
    #     header_obj = ''

    # menu_obj = Menu.objects.all().order_by('order');
    print ctx_location
    return {
        'SITE_ROOT_URL_S': 'http://%s/'%(current_site.domain),
        'SITE_ROOT_URL': 'http://%s'%(current_site.domain),
        'locations': ctx_location,
        # 'context_menu': menu_obj,
    }