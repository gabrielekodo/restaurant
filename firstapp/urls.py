from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns=[
 # path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
path('logout/', views.logout_view, name='logout'),
     path('login/',views.login_view,name='login'),
    path('home/',views.home, name='home'),
    path('register/',views.create_account,name='register'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('menu/',views.menu, name='menu'),
path('menu_item/<int:pk>',views.display_menu_item,name='menu_item'),
    path('recipes/',views.add_recipe,name='recipes'),
path('recipes/<str:id>',views.view_recipe,name='viewrecipe'),
path('recipes/update/<int:id>/', views.update_menu, name='update_menu'),
path('recipes/delete/<int:id>/', views.delete_menu, name='delete_menu'),
]