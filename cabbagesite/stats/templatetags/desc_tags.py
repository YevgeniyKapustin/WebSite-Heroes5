from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag()
def get_reverse_order_desc(desc):
    desc = desc.split('<br/>')
    desc.reverse()
    return mark_safe('<br/>-----------------------<br/>'.join(desc))
