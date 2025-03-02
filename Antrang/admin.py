from django.contrib import admin

# Register your models here.
from .models import Dept ,Student,Parti,Course,Event
admin.site.register(Dept)
admin.site.register(Student)
admin.site.register(Parti)
admin.site.register(Course)
admin.site.register(Event)
