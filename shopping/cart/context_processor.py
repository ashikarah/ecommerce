from .views import _cart_id
from .models import Cart, CartItem


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            car_item = CartItem.objects.all().filter(cart=cart[:1])
            for cart_items in car_item:
                item_count += cart_items.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)