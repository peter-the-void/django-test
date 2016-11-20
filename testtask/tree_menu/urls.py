from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name= 'hello_page'),
	url(r'^page/(?P<page>[0-9]+)/$', views.get_menu, name='post_menu'),
	url(r'^page/([0-9]+)/menu/(?P<menu_pk>[0-9]+)/item/(?P<item_pk>[0-9]+)',
		views.get_menu_items, name = 'post_menu_items')
]


