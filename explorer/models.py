from django.db import models

# Create your models here.

class Folder(models.Model) :

    name = models.CharField(max_length=255, blank=False)
    path = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) :
        return self.name