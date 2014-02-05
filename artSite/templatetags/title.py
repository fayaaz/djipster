from artSite.models import Title
from django import template

register = template.Library()

@register.simple_tag
def get_title():
    return Title.objects.all()[:1][0]