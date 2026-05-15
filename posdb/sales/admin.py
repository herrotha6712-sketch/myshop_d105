# sales/admin.py

from django.contrib import admin
from django.utils.html import format_html  # ចាំបាច់សម្រាប់បង្ហាញរូបភាពតូច (Thumbnail)
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # ១. បង្ហាញរូបភាពតូច (Thumbnail) នៅជួរមុខគេបង្អស់ក្នុងបញ្ជីផលិតផល
    list_display  = ['display_thumbnail', 'name', 'category', 'price', 'stock', 'is_active']
    list_filter   = ['category', 'is_active']
    search_fields = ['name', 'barcode']
    ordering      = ['name']

    # ២. បង្កើត Function សម្រាប់ទាញរូបភាពមកបង្ហាញ (Thumbnail)
    def display_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "No Image"
    
    # កំណត់ឈ្មោះឱ្យ Column រូបភាព
    display_thumbnail.short_description = 'រូបភាព'


class OrderItemInline(admin.TabularInline):
    """បង្ហាញ order items ផ្ទាល់នៅក្នុងទំព័រកែ Order"""
    model  = OrderItem
    extra  = 1  # ចំនួនជួរទទេសម្រាប់បន្ថែម item ថ្មី
    fields = ['product', 'quantity', 'unit_price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # បង្ហាញបញ្ជីការបញ្ជាទិញ
    list_display  = ['pk', 'cashier', 'status', 'created_at']
    list_filter   = ['status']
    search_fields = ['cashier__username', 'notes'] # កែ cashier ទៅ cashier__username ដើម្បី search តាមឈ្មោះ user
    ordering      = ['-created_at']
    
    # បង្ហាញទម្រង់សម្រាប់បន្ថែមទំនិញក្នុង Order (Inline)
    inlines       = [OrderItemInline]