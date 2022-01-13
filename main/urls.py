from django.urls import path
from .views import (OrderCreateView, StatusUpdateView, OrderListView, OrderDetailView, ClientOrdersView)

urlpatterns = [
    path('orders/', OrderListView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),
    path('orders/create/', OrderCreateView.as_view()),
    path('orders/update-status/<int:pk>/', StatusUpdateView.as_view()),
    path('orders/clients/<int:pk>/', ClientOrdersView.as_view()),

]
