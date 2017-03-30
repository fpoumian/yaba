from django.conf import settings
from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('yaba/partials/_header_nav_menu_items.html')
def show_nav_header_menu_items():
    menu_items = [
        {
            'label': 'home',
            'url': reverse('index')
        },
        {
            'label': 'about',
            'url': reverse('about')
        },
        {
            'label': 'contact',
            'url': reverse('contact')
        },
    ]

    return {
        'menu_items': menu_items
    }
