from tree_menu.models import MenuItem 
from django.db.models import Q


def indexing_tree(prt, ltk):
	rtk = ltk + 1

	if prt.children.exists():
		for obj in MenuItem.objects.filter(parent = prt).order_by('left_key'):
			rtk = indexing_tree(obj,rtk)

	MenuItem.objects.filter(pk=prt.pk).update(right_key=rtk, left_key=ltk)
	return rtk


def reindexing_subtree(key, flag, menu):
	criterion1 = Q(left_key__gte=key) & Q(from_menu=menu)
	criterion2 = Q(right_key__gte=key) & Q(from_menu=menu)
	for obj in MenuItem.objects.filter(criterion1):
		obj.left_key += 2*flag
		super(MenuItem, obj).save()

	for obj in MenuItem.objects.filter(criterion2):
		obj.right_key += 2*flag
		super(MenuItem, obj).save()


def rename_from_menu(parent, menu):
	
	if parent.children.exists():		
		for obj in MenuItem.objects.filter(parent = parent):
			rename_from_menu(obj, menu)
	else:
		MenuItem.objects.filter(pk = parent.pk).update(from_menu=menu)	


def get_all_children(item, childs_lst):

	lst = childs_lst
	if item.children.exists():
		for obj in MenuItem.objects.filter(parent = item):
			lst = get_all_children(obj, lst)

	childs_lst.append(item)
	return lst

def get_level(obj, level):

	lvl = level
	if obj.parent:
		lvl = get_level(obj.parent, lvl) + 1

	return lvl










