from django.contrib import admin
from moneyApp.models import Statement

class statementAdmin(admin.ModelAdmin):
    list_display = ['name','amount','catagory']
    list_per_page = 10
    list_editable = ['amount','catagory']
    list_filter = ['catagory','amount']
    search_fields = ['name']
    fields = ['catagory','name','amount']

# Register your models here.
admin.site.register(Statement,statementAdmin)