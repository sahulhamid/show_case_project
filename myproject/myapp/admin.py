from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(UserBio)
admin.site.register(UserPost)


