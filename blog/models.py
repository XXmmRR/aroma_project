from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class BlogModel(models.Model):
    tags = TaggableManager()
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    views = models.ManyToManyField(IpModel, related_name='post_views', blank=True)
    body = RichTextField(blank=True, null=True)
    about = models.TextField(max_length=50, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id,
                                            self.slug])

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()


class Comment(models.Model):
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
