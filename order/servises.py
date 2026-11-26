from order.models import Order, OrderItem, Payment, Status
from cart.models import CartItem, Cart
from cart.services import get_active_cart
from products.models import Product
from django.db import transaction


def get_payment(payment_id):
    payment = Payment.objects.get(id=payment_id)
    if not payment:
        raise
    return payment


def decrease_product_count(Cart):
    cart_items = CartItem.objects.filter(cart=Cart)
    for cart_item in cart_items:
        product = Product.objects.select_for_update().get(cart_item.product)
        product.count -= cart_item.quantity
        product.save()


def create_checkout(user):
    cart = get_active_cart(user)

    # cart_items = CartItem.objects.filter(cart=cart)
    cart_items = cart.cart_items.all()
    if not cart_items.exists():
        raise
    total_price = sum(
        item.get_total_price()
        for item in cart_items
    )
    order = Order.objects.create(
        user=user,
        total_price=total_price,
        cart= cart
    )
    order_items = []
    for cart_item in cart_items:
        order_items.append(
            OrderItem(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            unit_price=cart_item.product.price
        )
        )
    OrderItem.objects.bulk_create(order_items)

    payment = Payment.objects.create(
        order=order,
        amount=total_price,
    )
    return payment

def payment_succeed(payment_id):
    payment = get_payment(payment_id)
    with transaction.atomic():
        payment.status = Status.SUCCEED
        payment.save(update_fields=['status'])

        order = payment.order
        order.status = Status.SUCCEED
        order.save(update_fields=['status'])

        cart = order.cart
        cart.is_active = False
        cart.save(update_fields=['is_active'])

        decrease_product_count(cart)
    return payment

def payment_failed(payment_id):
    payment = get_payment(payment_id)
    with transaction.atomic():
        payment.status = Status.FAILED
        payment.save(update_fields=['status'])

        payment.status = Status.FAILED
        payment.save(update_fields=['status'])

        payment.order.status = Status.FAILED
        payment.order.save(update_fields=['status'])

    return payment