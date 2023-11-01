from django.urls import path


from .views import (
    renderFolderView,
    renderCreateFolderView,
    renderUploadFileView,
)


urlpatterns = [
    path('<folder_id>', renderFolderView, name='folder'),
    path('create-folder/<parent_id>', renderCreateFolderView, name='create-folder'),
    path('create-file/<parent_id>', renderUploadFileView, name='create-file'),
]