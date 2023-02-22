from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class TreeMenuAdmin(admin.ModelAdmin):

    fields = ['name', 'path', 'parent', ]
    list_display = ['__str__', 'path', 'parent', ]

    # filter_horizontal = ['category__name', ]