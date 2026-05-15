# sales/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem
from .forms import OrderItemForm


@login_required
def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'sales/product_list.html', {'products': products})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'sales/product_detail.html', {'product': product})


@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-id')
    return render(request, 'sales/order_list.html', {'orders': orders})


@login_required
def create_order(request):
    """Create new order and go to add item page"""

    order = Order.objects.create(
        cashier=request.user,
        status='open',
    )

    return redirect('add_item', pk=order.pk)


@login_required
def add_item(request, pk):

    order = get_object_or_404(Order, pk=pk)

    # POST
    if request.method == 'POST':

        # Mark order as paid
        if 'mark_paid' in request.POST:
            order.status = 'paid'
            order.save()

            return redirect('order_list')

        # Get data from form
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity', 1))

        # Find product
        product = get_object_or_404(Product, id=product_id)

        # Create OrderItem
        item = OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            unit_price=product.price
        )

        # Deduct stock
        product.stock -= quantity
        product.save()

        # Stay on same page
        return redirect('add_item', pk=order.pk)

    # GET
    products = Product.objects.filter(
        is_active=True,
        stock__gt=0
    )

    item_form = OrderItemForm()

    return render(request, 'sales/add_item.html', {
        'order': order,
        'products': products,
        'item_form': item_form,
        'items': order.items.all(),
    })


@login_required
def cancel_order(request, pk):
    """Cancel order and restore stock"""

    order = get_object_or_404(Order, pk=pk)

    # Restore stock
    for item in order.items.all():
        product = item.product
        product.stock += item.quantity
        product.save()

    # Change status
    order.status = 'cancelled'
    order.save()

    return redirect('order_list')


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        cashier=request.user
    ).order_by('-id')

    return render(request, 'sales/order_list.html', {
        'orders': orders
    })