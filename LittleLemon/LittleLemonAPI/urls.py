from django.urls import path
from . import views

def temp(request):
    pass
urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(),name='menu-items'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(),name='menu-item'),
    
    path('groups/manager/users/', views.ManagerUsersView.as_view(),name='manage-users'),
    path('groups/manager/users/<int:pk>/', views.ManagerSingleUserView.as_view(),name='manage-user'),
    
    path('groups/delivery-crew/users/', views.Delivery_crew_management.as_view(),name='deliveries-management'),
    path('groups/delivery-crew/users/<int:pk>/', views.Delivery_crew_management_single.as_view(),name='delivery-management'),
    
    path('cart/menu-items/', views.Customer_Cart.as_view(),name='customer-cart'),
    
    path('orders/', views.Orders_view.as_view(),name='orders'),
    path('orders/<int:pk>/', views.Single_Order_view.as_view(),name='order'),
]