from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
    list_display_links = ['name']
    search_fields = ['id','name','description']
class TeacherCourseAdmin(admin.ModelAdmin):
    list_display = ['id','user']
    list_display_links = ['user']
    search_fields = ['id','user']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name','course']
    list_display_links = ['name']
    search_fields = ['id','name','course']
class GroupStudentAdmin(admin.ModelAdmin):
    list_display = ['id','user','group']
    list_display_links = ['group']
    search_fields = ['id','group','user']
admin.site.register(Course,CourseAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(TeacherCourse,TeacherCourseAdmin)
admin.site.register(GroupStudent,GroupStudentAdmin)

