from django import template
from ..models import Review
from django.db.models import Avg

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

