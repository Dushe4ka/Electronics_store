from rest_framework.routers import SimpleRouter

from main.apps import MainConfig
from django.urls import path

from main.views import (
    ProductDestroyAPIView, ProductCreateAPIView, ProductListAPIView, ProductUpdateAPIView, ProductRetrieveAPIView,
    LinkListAPIView, LinkCreateAPIView, LinkRetrieveAPIView, LinkUpdateAPIView, LinkDestroyAPIView,
)

app_name = MainConfig.name

urlpatterns = [
    path("", LinkListAPIView.as_view(), name="link_list"),
    path("create/", LinkCreateAPIView.as_view(), name="link_create"),
    path("<int:pk>/", LinkRetrieveAPIView.as_view(), name="link_retrieve"),
    path("<int:pk>/update/", LinkUpdateAPIView.as_view(), name="link_update"),
    path("<int:pk>/delete/", LinkDestroyAPIView.as_view(), name="link_delete"),
    path("product-list/", ProductListAPIView.as_view(), name="product_list"),
    path("product/create/", ProductCreateAPIView.as_view(), name="product_create"),
    path("product/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product_retrieve"),
    path("product/<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDestroyAPIView.as_view(), name="product_delete"),
]