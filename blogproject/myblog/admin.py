from django.contrib import admin

# Register your models here.
from .models import Posts, UserRegistration

admin.site.register(Posts)
admin.site.register(UserRegistration)