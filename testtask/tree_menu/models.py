from django.db import models
from django.db.models import Q



class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	parent = models.ForeignKey('self', related_name='children', null=True, blank=True, default=None)
	url = models.CharField(max_length=100)
	left_key = models.IntegerField(blank=True, null=True)
	right_key = models.IntegerField(blank=True, null=True)
	from_menu = models.ForeignKey('Menu', default=None, null=True)
	level = models.IntegerField(blank=True)

	def __str__(self):
		return self.name


	def save(self, *args, **kwargs):
		if not self.pk:

			from .utils import reindexing_subtree, get_level

			if not self.parent:
				self.parent = MenuItem.objects.get(Q(left_key=1) & Q(from_menu=self.from_menu))

			self.left_key = self.parent.left_key + 1
			self.right_key = self.parent.left_key + 2
			reindexing_subtree(self.left_key, 1, self.from_menu)
			self.level = get_level(self,0)
			super(MenuItem, self).save(*args, **kwargs)
			
		else:
			old_menu = MenuItem.objects.get(pk=self.pk).from_menu
			old_parent = MenuItem.objects.get(pk=self.pk).parent

			if self.from_menu != old_menu:

				from .utils import rename_from_menu, indexing_tree, get_level

				if not self.parent:
					self.parent = MenuItem.objects.get(Q(left_key=1) & Q(from_menu=self.from_menu))
				self.level = get_level(self, 0)
				super(MenuItem, self).save(*args, **kwargs)
				rename_from_menu(self, self.from_menu)
				criterion = Q(from_menu=old_menu) & Q(left_key=1)
				indexing_tree(MenuItem.objects.get(criterion), 1)
				criterion = Q(from_menu=self.from_menu) & Q(left_key=1)
				indexing_tree(MenuItem.objects.get(criterion), 1)

			else:
				if self.parent != MenuItem.objects.get(pk=self.pk).parent:
					if not self.parent:
						self.parent = MenuItem.objects.get(Q(left_key=1) & Q(from_menu=self.from_menu))

					from .utils import indexing_tree, get_level

					self.level = get_level(self, 0)
					super(MenuItem, self).save(*args, **kwargs)
					criterion = Q(left_key=1) & Q(from_menu=self.from_menu)
					indexing_tree(MenuItem.objects.get(criterion), 1)


	def delete(self):
		from .utils import get_all_children, reindexing_subtree

		key = self.left_key
		menu = self.from_menu
		for obj in get_all_children(self,[]):
			super(MenuItem, obj).delete()
		reindexing_subtree(key, -1, menu)



class Menu(models.Model):
	name = models.CharField(max_length=100)
	page = models.CharField(max_length=100)
	root_item = models.ForeignKey('MenuItem', null=True, blank=True, editable=False)


	def __str__(self):
		return self.name


	def save(self, *args, **kwargs):
		root = MenuItem(name = self.name, url = self.page, left_key=1, right_key=2, level=0)
		super(MenuItem, root).save()
		self.root_item = root
		super(Menu, self).save(*args, **kwargs)
		root.from_menu = self
		super(MenuItem, root).save()


	def delete(self):
		from .utils import get_all_children

		for obj in get_all_children(self,[]):
			super(MenuItem, obj).delete()

		super(Menu, self).delete()
		
		


















	























