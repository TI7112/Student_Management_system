from django.contrib import admin
from App.models import Students

class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'father_name', 'contact', 'city',)

# Register your models here.

admin.site.register(Students , StudentAdmin)