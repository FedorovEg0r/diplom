from django.contrib import admin
from .models import ParserSetting


@admin.register(ParserSetting)
class ParserSettingAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'groups', 'keywords', 'excludes')
    search_fields = ('user',)
