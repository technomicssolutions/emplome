from django.contrib import admin
from web.models import *

class JobSeekerProfileAdmin(admin.ModelAdmin):

    list_filter = ('age',)




admin.site.register(UserProfile)
admin.site.register(Employment)
admin.site.register(Education)
admin.site.register(CompanyProfile)
admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)
admin.site.register(RecruiterProfile)
admin.site.register(Job)
admin.site.register(SuccessStory)
admin.site.register(Recommendation)
admin.site.register(PreviousEmployer)
admin.site.register(Doctorate)





