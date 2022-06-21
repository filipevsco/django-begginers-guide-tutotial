from libgravatar import Gravatar
from django import template

register = template.Library()


@register.filter
def gravatar(user):
    email = user.email.lower()
    g = Gravatar(email)
    return g.get_image()