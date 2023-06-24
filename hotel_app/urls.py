from django.urls import path
from . import views
from users import views as users_views

urlpatterns =[
    path('', views.home, name='hotel-home'),
    path('regsiter/',users_views.register, name='register')
]