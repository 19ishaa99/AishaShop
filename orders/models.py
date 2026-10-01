
from django.db import models
from blog.models import Product

class Order(models.Model):
    buyer_name = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

   
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    payment_status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Paid', 'Paid')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order #{self.id} by {self.buyer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)

        # Trigger recalculation of order total
        self.order.save()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"
