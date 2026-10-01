
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('price', 'total')
    autocomplete_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer_name', 'email', 'payment_status', 'total_price', 'created_at')
    list_filter = ('payment_status', 'created_at')
    search_fields = ('buyer_name', 'email', 'recipient_name', 'city')
    inlines = [OrderItemInline]
    readonly_fields = ('total_price',)

admin.site.register(Order, OrderAdmin)
