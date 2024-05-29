from django.urls import path
from .api_views import ItemListCreateAPIView, ItemDetailView, CategoryListView

urlpatterns = [
    path('items/', ItemListCreateAPIView.as_view(), name='api_item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='api_item_detail'),
    path('categories/', CategoryListView.as_view(), name='api_category_list'),
]
