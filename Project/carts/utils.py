from .models import Cart


def get_or_create_cart(request):
    # Lo reescribi de nuevo porque reabri el codigo y no lo entendia jaja
    # request.session['cart_id'] = None
    user = request.user if request.user.is_authenticated else None
    # Esto retorna None en caso la llave no exista
    cart_id = request.session.get('cart_id')
    # El metodo filter devuelve una lista de objetos PERO me permite usar el filter, y si filter no encuentra en el no se encuentra carrito retorna None
    cart = Cart.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id
    return cart
