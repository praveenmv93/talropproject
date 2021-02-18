from django.contrib import admin

# Register your models here.
from .models import Posts, UserRegistration, Staff

admin.site.register(Posts)
admin.site.register(UserRegistration)
admin.site.register(Staff)