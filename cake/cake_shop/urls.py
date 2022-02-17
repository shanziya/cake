from .import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'cake_shop'

urlpatterns = [
    path('', views.cakeprodct,name='cakeprodct'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('cake_order_page/',views.cake_order_page,name='cake_order_page'),
    path('cake_list_page/',views.cake_list_page,name='cake_list_page'),
    path('places/',views.cake_list_places,name='cake_list_places'),

]