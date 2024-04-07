from rest_framework import serializers

from .models import *
from decimal import Decimal

from datetime import datetime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','featured','category']

class CartSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='menuitem.price',read_only=True)
    
    class Meta:
        model = Cart
        fields=["user_id",'menuitem','quantity','unit_price','price']
        extra_kwargs={
            'price':{'read_only':True}
        }

class OrderItemSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='menuitem.price',read_only=True)
    class Meta:
        model  = Order
        fields =  ['menuitem', 'quantity', 'unit_price', 'price']


class OrdersSerializer(serializers.ModelSerializer):
    Date = serializers.SerializerMethodField(method_name='get_Date')
    date = serializers.DateTimeField(write_only=True, default=datetime.now)
    order_items = serializers.SerializerMethodField(method_name='get_order_items')

    class Meta:
        model = Order
        fields = ['id','user','delivery_crew','status','total','date','order_items']
        extra_kwargs = {
            'total': {'read_only': True}
        }

    def get_Date(self, obj):
        return obj.date.strftime('%Y-%m-%d')

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(order_items, many=True, context={'request': self.context['request']})
        return serializer.data

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']
