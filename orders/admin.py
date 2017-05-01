from django.contrib import admin
from .models import Order
from .models import OrderItem


class OrderItemInline(admin.TabularInline):
    """Allows to include a model on the same edit page as the parent model"""
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    """Modifies orders display in admin section"""
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
