from django.urls import path
from .views import *

urlpatterns = [
    path('', StockListView.as_view(), name='stock-list'),
    path('add/', StockCreateView.as_view(), name='stock-add'),
    path('edit/<int:pk>/', StockUpdateView.as_view(), name='stock-edit'),
    path('delete/<int:pk>/', StockDeleteView.as_view(), name='stock-delete'),
    path('upload/', upload_excel, name='upload-excel'),
    path('download-excel/',download_excel, name='download-excel'),
]
