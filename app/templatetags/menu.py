from django import template

from app.models import SubMenu, Menu

register = template.Library()


@register.inclusion_tag('template_tags/menu.html', takes_context=True)
def menu(context):
    all_menus_and_submenus = Menu.objects.all().prefetch_related('submenu').order_by('order_number')
    slug = context.request.GET.get('menu')
    return {'menus': all_menus_and_submenus, 'slug': slug}
