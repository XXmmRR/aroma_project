from django import template
from ..models import Review
from django.db.models import Avg
from cart.cart import Cart

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.simple_tag
def total_posts(pk):
    return Review.objects.filter(post__id=pk).count()


@register.simple_tag
def avg_rate(pk):
    reviews = Review.objects.filter(post__id=pk)
    average = reviews.aggregate(average=Avg('rate'))
    return average['average']


@register.simple_tag(takes_context=True)
def cart_total_amount(context):
    request = context['request']
    if request.user.is_authenticated:
        cart = Cart(request)
        total_bill = 0.0
        for key,value in request.session['cart'].items():
            total_bill = total_bill + (float(value['price']) * value['quantity'])
        return total_bill
    else:
        return {'cart_total_amount' : 0}
