from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_type')
    title = models.CharField(max_length=50)
    price = models.DecimalField()
    Count = models.DecimalField()
    Description = models.TextField(max_length=500)
    Character = models.TextField(max_length=500)
