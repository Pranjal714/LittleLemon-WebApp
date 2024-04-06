from django.contrib import admin
#from .views import sayHello
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =  [
    #path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.singleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]