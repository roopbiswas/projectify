from django.contrib import admin

from .models import Mentor
from .models import Student

admin.site.register(Mentor)
admin.site.register(Student)
