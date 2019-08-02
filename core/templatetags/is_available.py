import datetime
import pdb

from django import template

from core.models import Seat

register = template.Library()


@register.simple_tag(takes_context=True)
def is_available(context):
    seat = context['seat']
    showtime = context['showtime']
    return False if seat.item.filter(showtime=showtime) else True
