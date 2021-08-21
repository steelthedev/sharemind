from django.db import models

# Create your models here.\

import string
import random
from django.utils.text import slugify



def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))




class Experience(models.Model):
    title= models.CharField(max_length=200 , blank=False , null=False)
    #category = models.ForeignKey("Categories", blank=False , null=True , on_delete=models.SET_NULL)
    category = models.CharField(max_length=200 , blank=False , null=True)
    post = models.TextField(blank=False , null=False)
    slug = models.SlugField(null=True)
    comments = models.ForeignKey("Comment", null=True, on_delete=models.SET_NULL )
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
            super(Experience, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return self.title

class Categories(models.Model):
    name = models.CharField(max_length=100 , blank=False , null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
class Comment(models.Model):
    text = models.TextField(blank=False , null=False)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Experience , on_delete=models.CASCADE)
    active = models.BooleanField(null=True , blank=False)
    def __str__(self) -> str:
        return self.text
