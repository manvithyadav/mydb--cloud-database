from django.contrib import admin

from .models import (
    DBUser,
)


# Register your models here.

admin.site.register(DBUser)