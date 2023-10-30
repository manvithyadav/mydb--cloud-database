from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Folder(models.Model) :

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

    name = models.CharField(max_length=255, blank=False)
    path = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) :
        return self.name
    

