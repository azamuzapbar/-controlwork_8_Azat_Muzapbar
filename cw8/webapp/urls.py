from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.products import ProductCreateView, ProductDeleteView, ProductUpdateView, ProductDetailView
from .views.base import IndexView
from .views.reviews import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='confirm_delete'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/review/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('product/<int:pk>/review/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
