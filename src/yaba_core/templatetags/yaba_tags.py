from django.conf import settings
from django import template

register = template.Library()


@register.inclusion_tag('yaba/partials/_header_nav_menu_items.html')
def show_nav_header_menu_items():
    return {
        'menu_items': settings.YABA_HEADER_NAV_ITEMS
    }
