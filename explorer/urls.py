from django.urls import path


from .views import (
    renderFolderView,
    renderCreateFolderView,
    renderUploadFileView,
    renderDeleteFileView,
    renderRestoreFileView,
)


urlpatterns = [
    path('<folder_id>', renderFolderView, name='folder'),
    path('create-folder/<parent_id>', renderCreateFolderView, name='create-folder'),
    path('create-file/<parent_id>', renderUploadFileView, name='create-file'),
    path('delete-file/<parent_id>/<file_id>', renderDeleteFileView, name='delete-file'),
    path('restore-file/<parent_id>/<file_id>', renderRestoreFileView, name='restore-file'),
]