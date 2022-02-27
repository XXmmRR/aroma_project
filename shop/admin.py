from django.contrib import admin
from .models import Category, Product, Comment, Review

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'Description')
    list_filter = ('created', 'publish', 'Description')
    search_fields = ('title', 'Description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Review)

