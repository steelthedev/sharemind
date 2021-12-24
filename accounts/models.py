from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length = 250)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user