from .cart import Cart


def cart(request):
    """Makes 'cart' available for all templates"""
    return {'cart': Cart(request)}
