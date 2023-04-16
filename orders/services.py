from .models import Order
from rest_framework.response import Response
from rest_framework import status


def validate_order(pk, cur_status: str, courier_id: int = None):
    order = Order.objects.filter(id=pk).first()
    if not order:
        return Response(
            {'error': 'Order not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if order.status != cur_status:
        return Response(
            {'error': 'Order is not available'},
            status=status.HTTP_400_BAD_REQUEST
        )

