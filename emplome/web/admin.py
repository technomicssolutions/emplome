from django.contrib import admin
from web.models import *

# class UserProfileAdmin(admin.ModelAdmin):

#     list_filter = ('age',)

class EmploymentAdmin(admin.ModelAdmin):

	list_filter = ('skills',)

class EducationAdmin(admin.ModelAdmin):

	list_filter = ('resume_title',)




# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(CompanyProfile)
admin.site.register(Job)
admin.site.register(SuccessStory)
admin.site.register(Recommendation)





