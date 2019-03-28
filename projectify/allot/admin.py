from django.contrib import admin

from .models import Mentor
from .models import Student
from .models import Notifications

admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Notifications)