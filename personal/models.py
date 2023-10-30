from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DBUser(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    name = models.CharField(max_length=50, blank=False)

    root_id = models.CharField(max_length=50, blank=False)

    def __str__(self) :
        return self.name