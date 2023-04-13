from django.contrib import admin
from .models import Page


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('tittle', 'order')

admin.site.register(Page, PageAdmin)