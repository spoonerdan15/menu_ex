import re

from django import template
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch

from ..models import *

register = template.Library()


@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = '', parent: int = 0):

    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:
        is_url = re.compile(r'^http[s]?://')

        data = Menu.objects.all()

        menu = []

        for item in data:

            path = item.path.strip()

            target = '_self'

            if is_url.match(path):
                url = path
                target = '_blank'
            else:
                try:
                    url = reverse(path)
                except NoReverseMatch:
                    url = path

            menu.append({
                'id': item.pk,
                'url': url,
                'target': target,
                'name': item.name,
                'parent': item.parent_id or 0,
            })
    return {
        'menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }