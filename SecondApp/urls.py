from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('user_home/', views.user_home, name='user_home'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    
   
]























# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.main_home, name='main_home'),
#     path('user/', views.user_home, name='user_home'),
#     path('dealer/', views.dealer_home, name='dealer_home'),
#     path('registration/', views.registration, name='registration'),
#     path('login/', views.login, name='login'),
# ]
