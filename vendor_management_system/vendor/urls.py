from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet,UserRegistartion,PurchaseOrderViewset


# create a router it automatically generate the url
router=DefaultRouter()
router.register(r"vendors",VendorViewSet,basename='vendors'),
router.register(r"purchaseorder",PurchaseOrderViewset,basename='purchaseorder')

urlpatterns = [

   path("",include(router.urls)),
   path("userregisration",UserRegistartion.as_view(),name="userRegistation")
]
