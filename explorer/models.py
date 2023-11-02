from django.db import models
from django.contrib.auth.models import User

# Create your models here.


FILE_TYPE = (
    ('text', 'text'),
    ('html', 'html'),
    ('css', 'css'),
    ('js', 'js'),
    ('ppt', 'ppt'),
    ('pdf', 'pdf'),
)

class Folder(models.Model) :

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

    name = models.CharField(max_length=255, blank=False)
    path = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) :
        return self.name
    

class File(models.Model) :

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

    name = models.CharField(max_length=255, blank=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=255, blank=False, choices=FILE_TYPE)

    file = models.FileField(null=True, blank=False)

    # no need of path for a file (as it is folder path + file name)
    
    def __str__(self) :
        return self.name