# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.main_home, name='main_home'),
#     path('registration/', views.registration, name='registration'),
#     path('login/', views.user_login, name='login'),
#     path('user_home/', views.user_home, name='user_home'),
#     path('product_list/', views.product_list, name='product_list'),
#     path('add_product/', views.add_product, name='add_product'),
#     path('update_product/<int:product_id>/', views.update_product, name='update_product'),
#     path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
#     path('search/', views.product_search, name='product_search'),

#     path('wishlist/', views.wishlist, name='wishlist'),
#     path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
#     path('remove-from-wishlist/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
#     path('logout/', views.logout_view, name='logout'),
#     path('update-user-details/', views.update_user_details, name='update_user_details'),
#     path('change_password/', views.change_password, name='change_password'),


#     path('category/', views.category_list, name='category_list'),
#     path('category/<int:category_id>/', views.category_detail, name='category_detail'),
#     path('category/add/', views.add_category, name='add_category'),
#     path('category/update/<int:category_id>/', views.update_category, name='update_category'),
#     path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    

#     path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


# ]



# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('', views.main_home, name='main_home'),
# #     path('user/', views.user_home, name='user_home'),
# #     path('dealer/', views.dealer_home, name='dealer_home'),
# #     path('registration/', views.registration, name='registration'),
# #     path('login/', views.login, name='login'),
# # ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/update_address/', views.update_address, name='update_address'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/<int:category_id>/update/', views.update_category, name='update_category'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('user_home/', views.user_home, name='user_home'),
    path('update_user_details/', views.update_user_details, name='update_user_details'),
    path('change_password/', views.change_password, name='change_password'),
    path('product/list/', views.product_list, name='product_list'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/<int:product_id>/update/', views.update_product, name='update_product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/search/', views.product_search, name='product_search'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:cart_item_id>/', views.update_cart_item, name='update_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('main_home/', views.main_home, name='main_home'),  # Assuming this is the landing page
    path('update_address/', views.update_address, name='update_address'),  # Duplicate, remove if unnecessary

    
]