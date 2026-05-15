# sales/urls.py — ឯកសារពេញលេញដែលបូកបញ្ចូលមុខងារ Cancel Order

from django.urls import path
from . import views

urlpatterns = [
    # --- ផ្នែកទី 1: ការបង្ហាញទិន្នន័យ (Viewing Data) ---
    # បង្ហាញបញ្ជីផលិតផលទាំងអស់
    path('products/', views.product_list, name='product_list'),
    
    # បង្ហាញព័ត៌មានលម្អិតនៃផលិតផលមួយ (តាមរយៈ ID/PK)
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    
    # បង្ហាញបញ្ជីការបញ្ជាទិញ (Orders) ទាំងអស់
    path('orders/', views.order_list, name='order_list'),

    # --- ផ្នែកទី 2: ដំណើរការលក់ (POS Transactions) ---
    # បង្កើតការបញ្ជាទិញថ្មី (ទំព័រចាប់ផ្តើមលក់)
    path('orders/new/', views.create_order, name='create_order'),
    
    # បន្ថែមមុខទំនិញចូលក្នុង Order (ឧទាហរណ៍៖ orders/3/items/)
    path('orders/<int:pk>/items/', views.add_item, name='add_item'),
    
    # បោះបង់ការបញ្ជាទិញ (Cancel Order) និងបង្វិលស្តុកចូលវិញ
    path('orders/<int:pk>/cancel/', views.cancel_order, name='cancel_order'),
    
    # មើលបញ្ជីលក់ផ្ទាល់ខ្លួនរបស់បេឡាករ (Cashier) ដែលកំពុង Login
    path('orders/mine/', views.my_orders, name='my_orders'),
]