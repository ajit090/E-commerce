from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
<<<<<<< HEAD
=======
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
>>>>>>> edd878153edb8a33fb3c45db5df0cf41352d1cdd
from .models import UserProfile,Item,OrderItem,Payment,Address,Order
from .serializers import UserProfileSerializer,ItemSerializer,OrderItemSerializer,OrderSerializer,AddressSerializer,PaymentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
<<<<<<< HEAD
from rest_framework.views import APIView
=======
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
>>>>>>> edd878153edb8a33fb3c45db5df0cf41352d1cdd


class UserProfileAPIView(APIView):

    def get(self,request):
        userprofile = UserProfile.objects.all()
<<<<<<< HEAD
        serializer = UserProfileSerializer(userprofile,many=True)
=======
        serializer = UserProfileSerializer(userprofile, many=True)
>>>>>>> edd878153edb8a33fb3c45db5df0cf41352d1cdd
        return Response(serializer.data)

    
    
    def post(self,request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def User_list(request):

    if request.method=='GET':
        userprofile = UserProfile.objects.all()
<<<<<<< HEAD
        serializer = UserProfileSerializer(userprofile,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=UserProfileSerializer(data=request.data)
=======
        serializer = UserProfileSerializer(companys,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=UserProfileSerializer(data=request.data)

>>>>>>> edd878153edb8a33fb3c45db5df0cf41352d1cdd
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def UserProfile_detail(request, pk):
    try:
        userprofile = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(userprofile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        userprofile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ItemAPIView(APIView):
    def get(self,request):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data) 

    
    
    def post(self,request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def Item_list(request):
<<<<<<< HEAD
=======

>>>>>>> edd878153edb8a33fb3c45db5df0cf41352d1cdd
    if request.method=='GET':
        item = Item.objects.all()
        serializer = ItemSerializer(item,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
<<<<<<< HEAD
        serializer=ItemSerializer(item,data=request.data)
=======
        serializer=ItemSerializer(data=request.data)

>>>>>>> edd878153edb8a33fb3c45db5df0cf41352d1cdd
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def Item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
<<<<<<< HEAD
        serializer = ItemSerializer(data=request.data)
=======
        serializer = ItemSerializer(item,data=request.data)
>>>>>>> edd878153edb8a33fb3c45db5df0cf41352d1cdd
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemAPIView(APIView):
    def get(self,request):
        orderitem = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderitem, many=True)
        return Response(serializer.data) 

    
    
    def post(self,request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def OrderItem_list(request):

    if request.method=='GET':
        orderitem = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderitem,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=OrderItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def OrderItem_detail(request, pk):
    try:
        orderitem = OrderItem.objects.get(pk=pk)
    except OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderItemSerializer(orderitem)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(orderitem,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderAPIView(APIView):
    def get(self,request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data) 

    
    
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Order_list(request):

    if request.method=='GET':
        order =Order.objects.all()
        serializer = OrderSerializer(order,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def Order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddressAPIView(APIView):
    def get(self,request):
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data) 

    
    
    def post(self,request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Address_list(request):

    if request.method=='GET':
        address =Address.objects.all()
        serializer = AddressSerializer(address,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=AddressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Address_detail(request, pk):
    try:
        address = Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AddressSerializer(address)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AddressSerializer(address,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PaymentAPIView(APIView):
    def get(self,request):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data) 

    
    
    def post(self,request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Payment_list(request):

    if request.method=='GET':
        payment =Payment.objects.all()
        serializer = PaymentSerializer(payment,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=PaymentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Payment_detail(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PaymentSerializer(payment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


