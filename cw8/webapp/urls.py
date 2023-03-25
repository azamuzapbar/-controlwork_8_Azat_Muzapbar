from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.products import ProductCreateView, ProductDetail, ProductDeleteView, ProductUpdateView
from .views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='confirm_delete'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
