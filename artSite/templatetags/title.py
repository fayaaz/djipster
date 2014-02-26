from artSite.models import Title
from artSite.models import MainPicture
from django import template

register = template.Library()

@register.simple_tag
def get_title():
    return Title.objects.all()[:1][0]

@register.simple_tag
def get_main_img():
    return MainPicture.objects.all()[:1][0]