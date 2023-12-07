from django.urls import path
from .views import CustomerView,  CustomerUpdateView, ProductView, OrderListView

urlpatterns = [
    path('customers/', CustomerView.as_view(), name='customer-registrations'),
    path('customers/<int:id>/', CustomerUpdateView.as_view(), name='customer-update-view'),
    path('products/', ProductView.as_view(), name='product-create-view'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderListView.as_view(), name='order-detail'),
   

]