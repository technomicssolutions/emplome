from django.contrib import admin
from web.models import *

# class UserProfile(admin.ModelAdmin):
	
#     list_filter = ('court', 'sport')




admin.site.register(UserProfile)
admin.site.register(Employment)
admin.site.register(Education)
admin.site.register(CompanyProfile)
admin.site.register(Job)
admin.site.register(SuccessStory)
admin.site.register(Recommendation)





