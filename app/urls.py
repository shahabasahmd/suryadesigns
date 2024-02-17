from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views



urlpatterns = [
   
    path('',views.index,name='index'),
    path('products/',views.product_list_view,name='product-list'),
    path('product/<pid>/',views.product_detail_view,name='product_detail'),
  
    path('category/', views.category_list_view, name='category_list'),
    path('category/<cid>/', views.category_product_list_view, name='category_product_list'),
    path('add-to-wishlist/<int:pid>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/',views.wishlist_view, name='wishlist'),
    path('remove_from_wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add-review/', views.add_review, name='add_review'),
   
    # path('wishlist/',views.wishlist,name='wishlist'),

    # path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
  

    # path('search',views.search,name='search'),


    # path('numberplates',views.numberplates,name='numberplates'),
    # path('nameboards',views.nameboards,name='nameboards'),
    # path('gst_nameplates',views.gst_nameplates,name='gst_nameplates'),
    # path('number_signs',views.number_signs,name='number_signs'),

    # path('about',views.about,name='about'),

    # path('category',views.category,name='category'),

    # path('register',views.register,name='register'),
    # path('login',views.login,name='login'),

   


]


