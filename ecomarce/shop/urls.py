from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.categories),
    path('product/',views.product),
     path('cat_det/', views.select_category),
    path('products/', views.product_union_with_category),
    path('products_not/', views.not_product),
]

