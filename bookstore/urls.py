from . import views
from django.conf.urls import url

app_name = "bookstore"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insert/$', views.insert, name='insert'),
    url(r'^update/$', views.update, name='update'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^api/insert/$', views.insert_api, name='insert_api'),
    url(r'^api/update/(?P<book_id>[0-9]+)/$', views.update_api, name='update_api'),
    url(r'^api/delete/(?P<book_id>[0-9]+)/$', views.delete_api, name='delete_api'),
]
