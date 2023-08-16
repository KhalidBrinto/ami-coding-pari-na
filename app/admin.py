from django.contrib import admin
from .models import InputHistory, LoginHistory, UserProfile

# Register your models here.
admin.site.register(InputHistory)
admin.site.register(LoginHistory)
admin.site.register(UserProfile)
