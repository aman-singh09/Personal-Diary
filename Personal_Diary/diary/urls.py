from django.contrib import admin
from django.urls import path,include
from diary import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('',views.index,name='home'),
	path('new/',views.new,name='new'),
	path('about/',views.about,name='about-us'),
	path('show/<int:d_id>/',views.view,name='view'),
	path('register/',views.registration,name='register/'),
	path('login/',views.signin,name='login'),
	path('logout/',views.signout,name='logout'),
	path('home/', views.homepage, name = 'homepage'),
	path('accounts/login/', views.homepage),
]
