from django.urls import path
from .views import product_detail_view, products_list, upload_product
urlpatterns =[
    path("products/upload", upload_product, name="product_upload_view"),
    path ("products/list/", products_list, name="products_list"),
    path("products/<int:id>/", product_detail_view, name="product_details"),
]