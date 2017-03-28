from django import forms
from django.contrib import admin
from django.utils.timezone import now

from .models import Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['is_published', 'title', 'slug', 'excerpt', 'body']

        labels = {
            'is_published': 'Is published?',
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'

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

    def save_model(self, request, obj, form, change):
        if form.has_changed() and 'is_published' in form.changed_data:
            if obj.is_published:
                obj.pubished_at = now()
            else:
                obj.pubished_at = None

        super().save_model(request, obj, form, change)
