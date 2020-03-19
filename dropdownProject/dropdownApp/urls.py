from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax_handler/<int:id>',views.ajax_handler,name="ajax_handler")
]  