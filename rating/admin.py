from django.contrib import admin
from .models import *


class ForStatements(admin.ModelAdmin):
    search_fields = ['teacher__email','teacher__first_name', 'teacher__last_name']

class ForUsers(admin.ModelAdmin):
    search_fields = ['group__number', 'type_user', 'email', 'first_name', 'last_name']


admin.site.register(Disciplines)
admin.site.register(Faculties)
admin.site.register(Group)
admin.site.register(Users, ForUsers)
admin.site.register(Statements, ForStatements)
admin.site.register(Marks)
