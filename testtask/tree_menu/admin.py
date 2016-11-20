from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'parent', 'from_menu')
	



admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)

