from rest_framework import serializers
from .models import Vendors,PurchaseOrder
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
     model=User
     fields = ['username', 'password']
     
    

    def validate(self, data):
       username=data['username']
       if User.objects.filter(username=username).exists():
          raise serializers.ValidationError("User already exits......")
       return data
    


    def create(self, validated_data):
        user=User(
            username=validated_data['username'],
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
       

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendors
        fields = '__all__'

    
    def validate(self, data):
        name = data.get('name')
        contact_details = data.get('contact_details')
        address = data.get('address')

        if Vendors.objects.filter(name=name, contact_details=contact_details, address=address).exists():
            raise serializers.ValidationError("A vendor with the same name, contact details, and address already exists.")

        return data



class PoSerializer(serializers.ModelSerializer):
   class Meta:
        model=PurchaseOrder
        fields='__all__'