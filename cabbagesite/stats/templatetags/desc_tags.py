from django import template
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from reports.models import PlayerData

register = template.Library()


@register.simple_tag()
def get_reverse_order_desc(desc):
    desc = desc.split('<br/>')
    desc.reverse()
    return mark_safe('<br/>-----------------------<br/>'.join(desc))


@register.simple_tag()
def get_player_avatar(name):
    data = PlayerData.objects.filter(name=name)
    if data:
        return data[0].avatar.url
