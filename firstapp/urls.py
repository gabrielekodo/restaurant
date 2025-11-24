from django.urls import path
from . import views


urlpatterns=[
    path('home',views.home),
    path('about',views.about),
    path('booking',views.booking),
    path('menu',views.menu),
path('menu_item/<int:pk>',views.display_menu_item,name='menu_item')
]