from django import forms


from .models import (
    Folder,
)


class FolderCreationForm(forms.ModelForm) :

    class Meta :
        model = Folder
        fields = ('name',)