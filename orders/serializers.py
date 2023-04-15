from rest_framework import serializers
from .models import Order
from utils.models import Address


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'request_id',
            'courier_id',
            'address_id',
            'con_id',
            'client_iin',
            'taker_iin',
            'status',
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'oblast',
            'city',
            'street',
            'house_number',
            'apartment',
            'entrance',
            'floor',
            'housing',
            'residential_complex',
        ]


class OTPSerializer(serializers.Serializer):
    otp = serializers.CharField(
        max_length=6,
        min_length=6,
    )

