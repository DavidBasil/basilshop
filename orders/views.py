from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


def order_create(request):
    """Displays order form and sends confirmation email"""
    # get the current cart from the session
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
            cart.clear()
            # send confirmation email
            subject = 'Order nr. {}'.format(order.id)
            message = 'Dear {}, \n\nYou have successfully placed an order. \
                Your order id is {}'.format(order.first_name, order.id)
            mail_sent = send_mail(subject, message, 'admin@basilshop.com',
                                            [order.email])
            request.session['order_id'] = order.id
            # redirect to payment
            return redirect(reverse('payment:process'))
    else: 
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
