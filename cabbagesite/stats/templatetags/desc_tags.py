from django import template
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from reports.models import PlayerData

register = template.Library()


@register.simple_tag()
def get_reverse_order_desc(desc):
    desc = desc.split('<br/>').reverse()
    return mark_safe('<br/>-----------------------<br/>'.join(desc))


@register.simple_tag()
def get_player_avatar(name):
    return get_object_or_404(PlayerData, name=name).avatar
