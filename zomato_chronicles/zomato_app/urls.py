from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/<int:dish_id>/', views.menu_detail, name='menu_detail'),
    path('orders/', views.order_list, name='order_list'),
]
