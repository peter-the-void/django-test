from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def get_items_starttag(item):
	return format_html('<ul>'*item.level + '<li>')


@register.simple_tag
def get_items_endtag(item):
	return format_html('</li>' + '</ul>'*item.level)


@register.simple_tag
def edit_menu_url(menu):
	result = 'menu/' + str(menu.pk) + '/item/' + str(menu.root_item.pk)
	return result

@register.simple_tag
def edit_menuitem_url(menu_item):	
	return str(menu_item.pk)



@register.filter
def guards(item, key_item):
	if (item.level  <= key_item.level) or (item in key_item.children.all()):
		return True
	else:
		return False


