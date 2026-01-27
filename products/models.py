from django.db import models
from django.utils.text import slugify
from django.conf import settings
import os
from datetime import datetime

def upload_to(instance, filename):
    now = datetime.now()
    date_path = now.strftime('%Y/%m/%d')
    return os.path.join('uploads', date_path, filename)


class Product(models.Model):
    GAME_CHOICES = [
        ('pubg', 'PUBG'),
        ('cod', 'Call of Duty'),
        ('clash', 'Clash of Clans'),
    ]
    
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=upload_to)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    game_type = models.CharField(max_length=10, choices=GAME_CHOICES)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="options")
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    body = models.CharField(max_length=550)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to=upload_to)
    is_special_offer = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.title}"


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    rating = models.IntegerField(default=5)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="children")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
