from django.urls import path
from . import views 

urlpatterns = [
    path('user', views.get_user),
    path('get', views.get_data),
    path('add', views.add_data),
    path('del', views.delete_data),
    path('upd', views.update_data)
]
