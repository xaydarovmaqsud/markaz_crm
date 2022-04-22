from django.contrib import admin
from .models import User,Role,Permission,RolePermission,\
    UserRole, Tag, UserTag

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','phone_number','gender']
    list_display_links = ['phone_number']
    search_fields = ['id','username','phone_number']
    list_editable = ['username']

class PermissionTabular(admin.TabularInline):
    model = RolePermission


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
    list_display_links = ['name']
    search_fields = ['id','name','description']

    inlines = [PermissionTabular]


class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
    list_display_links = ['name']
    search_fields = ['id','name','description']


class UserTagAdmin(admin.ModelAdmin):
    list_display = ['id','user','tag']
    list_display_links = ['user']


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','model','name','description']
    list_display_links = ['name']
    search_fields = ['id','name','description']



admin.site.register(User,UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Permission,PermissionAdmin)
admin.site.register(RolePermission)
admin.site.register(UserRole)
admin.site.register(Tag,TagAdmin)
admin.site.register(UserTag, UserTagAdmin)


