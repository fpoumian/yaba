from django import forms
from django.contrib import admin
from django.db import models
from django.utils.timezone import now
from markdownx.admin import MarkdownxModelAdmin, AdminMarkdownxWidget

from .models import Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = []

        labels = {
            'is_published': 'Is published?',
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'

    fields = ('is_published', 'title', 'slug', 'featured_image', 'tags', 'excerpt', 'body', 'published_at')

    list_display = (
        'title',
        'is_published',
        'published_at',
        'created_at',
        'updated_at'
    )

    list_filter = ('is_published',)

    ordering = (
        '-published_at',
        '-created_at',
    )

    search_fields = (
        'title',
        'excerpt',
    )

    form = PostAdminForm

    prepopulated_fields = {
        'slug': ('title',)
    }

    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

    def save_model(self, request, obj, form, change):
        if form.has_changed() and 'is_published' in form.changed_data:
            if obj.is_published:
                obj.published_at = now()
            else:
                obj.published_at = None

        super().save_model(request, obj, form, change)
