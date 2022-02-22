from django.contrib import admin
from django.urls import path,include
from .views import ItemAPIView,Item,Item_detail,Item_list,OrderItemAPIView,OrderItem,OrderItem_list,OrderItem_detail,OrderItem,Order_list,OrderAPIView,Order_detail,AddressAPIView,Address_detail,Address_list,Payment,Payment_list,Payment_detail,PaymentAPIView


urlpatterns = [
    path('Item/',ItemAPIView.as_view()),
    path('detail/<int:pk>/',Item_detail),
    path('OrderItem/',OrderItemAPIView.as_view()),
    path('detail2/<int:pk>/',OrderItem_detail),
    path('Order/',OrderAPIView.as_view()),
    path('details/<int:pk>/',Order_detail),
    path('Address',AddressAPIView.as_view()),
    path('detail3/<int:pk>/',Address_detail),
    path('Payment/',PaymentAPIView.as_view()),
    path('detail4/<int:pk>/',Payment_detail)
    
    ]