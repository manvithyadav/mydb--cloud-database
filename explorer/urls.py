from django.urls import path


from .views import (
    renderFolderView,
    renderCreateFolderView,
    renderCreateFileView,
)


urlpatterns = [
    path('<folder_id>', renderFolderView, name='folder'),
    path('create-folder/', renderCreateFolderView, name='create-folder'),
    path('create-file/', renderCreateFileView, name='create-file'),
]