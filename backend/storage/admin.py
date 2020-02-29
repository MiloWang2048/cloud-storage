from django.contrib import admin
from django.utils.html import format_html

from mptt.admin import DraggableMPTTAdmin

from .models import File, Identifier

# Register your models here.

@admin.register(File)
class MyFile(admin.ModelAdmin):
    list_display = (
        'file',
        'size',
        'date_joined',
        'reference_count',
        'is_legal'
    )

@admin.register(Identifier)
class Catalogue(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'id')
    list_display_links = ('indented_title', 'id')

    def title(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )
    title.short_description = '文件（夹）名'
