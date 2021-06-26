from django.contrib import admin

from .models import Masterdata5, Mark_Attendance2
# Register your models here.

admin.site.register(Masterdata5)
#admin.site.register(Mark_Attendance2)
@admin.register(Mark_Attendance2)
class StudentAdmin(admin.ModelAdmin):
	list_display= ['roll_number','class_name','subject','time1','ip_address','date1','platform','Master',]
