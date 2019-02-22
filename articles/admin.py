from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article

class ArticleAdmin(SummernoteModelAdmin):
    search_fields = ('title', )
    list_display = ('author', 'title', 'is_display', 'is_index', )
    list_filter = ('is_display', 'is_index', )
    list_editable = ('is_display', 'is_index', )
    summernote_fields = ('content', )

admin.site.register(Article, ArticleAdmin)