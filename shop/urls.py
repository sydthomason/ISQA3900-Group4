from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('collections/<slug:collection_slug>/', views.product_list, name='product_list_by_collection'),  # Updated path for collections
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),  # Updated path for product detail
]
