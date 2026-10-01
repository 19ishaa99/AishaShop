from rest_framework import serializers
from .models import Order, OrderItem
# from .tasks import send_order_confirmation_email

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price', 'total']
        read_only_fields = ['price', 'total']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'buyer_name', 'recipient_name', 'address', 'city', 'postal_code',
            'email', 'phone_number', 'payment_status', 'created_at', 'total_price', 'items'
        ]
        read_only_fields = ['total_price', 'created_at']

    def validate(self, data):
        items = data.get('items', [])
        if not items:
            raise serializers.ValidationError("Order must contain at least one item.")
        return data

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total = 0
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price
            total += price * quantity
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price,
                total=price * quantity
            )
        order.total_price = total
        order.save()
        # Trigger asynchronous email sending
        # send_order_confirmation_email.delay(order.email, order.id, order.buyer_name)    
        return order
