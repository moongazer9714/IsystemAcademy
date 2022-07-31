import imp
from django.contrib import admin
from courses.models import Contact, Course
# Register your models here.

admin.site.register(Course)
admin.site.register(Contact)