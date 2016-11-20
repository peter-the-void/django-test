from django.shortcuts import render
from .models import Menu, MenuItem

def index(request):
	return render(request, 'tree_menu/index.html', {})


def get_menu(request, page):
	menus = Menu.objects.filter(page = page)
	return render(request, 'tree_menu/post_menu.html', {'menus': menus})


def get_menu_items(request, menu_pk, item_pk):
	key_item = MenuItem.objects.get(pk = item_pk)
	menu_items = MenuItem.objects.filter(from_menu = menu_pk).order_by('left_key')

	return render(request, 'tree_menu/post_menu_items.html', {'menu_items': menu_items, 'key_item': key_item})

