from django import template
import mistune

register = template.Library()


@register.filter(name='markdown')
def markdown(value):
    markdown = mistune.Markdown()
    return markdown(value)
