from django import forms


from .models import (
    Folder,
    File,
)


class FolderCreationForm(forms.ModelForm) :

    class Meta :
        model = Folder
        fields = ('name',)


class FileUploadForm(forms.ModelForm) :
    
    class Meta :
        model = File
        fields = ('name', 'file_type')