from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets,generics,status,filters
from rest_framework.response import Response
from .models import Vendors,PurchaseOrder
from .serializers import VendorSerializer,UserSerializer,PoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as django_filters
# Create your views here.

# creating the user signup using the django build model of User
class UserRegistartion(generics.GenericAPIView):
    serializer_class=UserSerializer
    permission_classes = [AllowAny]
    def post(self,request,*args, **kwargs):
        Serializer=self.get_serializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response({
                "message":'user regirsation is succefull...'
            },status.HTTP_201_CREATED)



class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendors.objects.all()
    serializer_class = VendorSerializer
    permission_classes=[IsAuthenticated]



class PurchaseOrderViewset(viewsets.ModelViewSet):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PoSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = [django_filters.DjangoFilterBackend]

