from django.contrib import admin
from django.urls import path,include
from diary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('new/',views.new,name='new'),
    path('about/',views.about,name='about-us')
]
