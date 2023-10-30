from django.shortcuts import render, redirect

from .models import (
    Folder,
)



APPNAME = 'explorer'

# Create your views here.

# def getParentPath(current) :
#     parent = curr
#     while parent is not None :


def renderFolderView(request, folder_id) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    context = {}

    try :
        folder = Folder.objects.get(id=folder_id)

        parent = folder.parent
        
        parents = []
        
        while parent is not None :
            parents.append(parent)
            parent = parent.parent

        context['parents'] = parents

        # get all files in the folder

        return render(request, APPNAME + '/folder.html', context)

    
    except Folder.DoesNotExist :
        print("Folder does not exist")
        redirect('home')



def renderCreateFolderView(request) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    context = {}

    return render(request, APPNAME + '/create_folder.html', context)


def renderCreateFileView(request) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    context = {}

    return render(request, APPNAME + '/create_file.html', context)