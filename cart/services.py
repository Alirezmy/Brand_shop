from products.models import Product
from cart.models import Cart, CartItem
from django.db import transaction


@transaction.atomic
def add_to_cart(user, product_id, quantity):
    product = Product.objects.get(id=product_id)
    if quantity > product.count:
        raise
    cart, created = Cart.objects.get_or_create(user=user, is_active=True)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += quantity
        if cart_item.quantity > product.count:
            raise
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return cart_item
