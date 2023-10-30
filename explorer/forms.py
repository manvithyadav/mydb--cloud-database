from django import forms


from .models import (
    Folder,
)


class CreateFolderForm(forms.ModelForm) :

    class Meta :
        model = Folder
        fields = ('name',)