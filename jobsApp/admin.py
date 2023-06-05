from django.contrib import admin
from .models import Job,  Category, Apply
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_type', 'vacancy', 'salary', 'experience',]
    list_filter = ['job_type']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ApplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'cd', 'created_at' ]
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Apply)
