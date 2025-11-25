from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns=[
 path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # path('login',views.login_view,name='login'),
    path('home',views.home, name='home'),
    path('register',views.create_account,name='register'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('menu',views.menu, name='menu'),
path('menu_item/<int:pk>',views.display_menu_item,name='menu_item')
]