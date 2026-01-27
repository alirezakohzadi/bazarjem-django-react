from django.db import models
from ckeditor.fields import RichTextField
import os
from django.utils.text import slugify
from datetime import datetime


def upload_to(instance, filename):
    now = datetime.now()
    date_path = now.strftime('%Y/%m/%d')
    return os.path.join('uploads', date_path, filename)


class Blogs(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_to)    
    content = RichTextField(default="")

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.name
        