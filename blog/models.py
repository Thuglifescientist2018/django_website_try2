from typing import runtime_checkable
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = RichTextField(blank=True, null=True)
