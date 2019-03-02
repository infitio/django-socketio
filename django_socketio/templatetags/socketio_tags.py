from os import environ

from django import template

from django_socketio.settings import PORT

register = template.Library()


@register.inclusion_tag("socketio_scripts.html", takes_context=True)
def socketio(context):
    context["DJANGO_SOCKETIO_PORT"] = environ.get("DJANGO_SOCKETIO_PORT", PORT)
    return context
