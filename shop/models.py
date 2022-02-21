from django.db import models
from django.utils import timezone
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_type')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Count = models.DecimalField(max_digits=6, decimal_places=2)
    Description = models.TextField(max_length=500)
    Character = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/shop', blank=True)
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('single_shop', args=[self.id,
                                            self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    body = models.TextField(max_length=400)
    avatar = models.ImageField(upload_to='images/shop/comments', blank=True)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
