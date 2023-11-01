from django.shortcuts import render, redirect

from .models import (
    Folder,
    File,
)

from .forms import (
    FolderCreationForm,
    FileUploadForm,
)


APPNAME = 'explorer'

# Create your views here.

# def getParentPath(current) :
#     parent = curr
#     while parent is not None :


def renderFolderView(request, folder_id) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    if request.user.is_superuser :
       return redirect('home')
    
    context = {}

    print(f'session is {request.session}')

    try :
        folder = Folder.objects.get(id=folder_id)

        parent = folder.parent
        
        parents = []
        
        while parent is not None :
            parents.append(parent)
            parent = parent.parent

        context['parents'] = parents
        context['folder'] = folder

        children = folder.folder_set.all()
        context['children'] = children

        files = folder.file_set.all()
        context['files'] = files

        # get all files in the folder

        # print(type(request.user.dbuser.root_id), type(folder.id))

        return render(request, APPNAME + '/folder.html', context)

    
    except Folder.DoesNotExist :
        print("Folder does not exist")
        redirect('home')



def renderCreateFolderView(request, parent_id) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    if request.user.is_superuser :
       return redirect('home')

    
    context = {}
    parent = Folder.objects.get(id=parent_id)
    context['folder'] = parent



    if request.method == 'POST' :
        folderCreationForm = FolderCreationForm(request.POST)
        if folderCreationForm.is_valid() :

            folder = Folder.objects.create(
                user=request.user,
                name=request.POST['name'],
                path=parent.path + request.POST['name'] + '/',
                parent=parent,
            )

            print("folder created")

            print(f'parent is {parent} and folder is {folder}')

            # after creating a new folder, we need to send to page of new folder

            context['folder'] = folder
            context['parent'] = parent

            # request.session['context'] = context
            request.session['folder_id'] = context['folder'].id
            request.session['parent_id'] = context['parent'].id

            return redirect('folder', folder_id=folder.id)

            # return render(request, APPNAME + '/folder.html', context)
        
        else :
            print("form invalid")
            folderCreationForm = FolderCreationForm()
            context['folderCreationForm'] = folderCreationForm
            
        
    else :
        folderCreationForm = FolderCreationForm()
        context['folderCreationForm'] = folderCreationForm

    return render(request, APPNAME + '/create_folder.html', context)


def renderUploadFileView(request, parent_id) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    if request.user.is_superuser :
       return redirect('home')
    
    context = {}
    parent = Folder.objects.get(id=parent_id)
    context['folder'] = parent


    if request.method == 'POST' :
        fileUploadForm = FileUploadForm(request.POST)
        if fileUploadForm.is_valid() :
            # create a file
            # store folder_id and parent_id in session
            # redirect to folder

            file = File.objects.create(
                user=request.user,
                name=request.POST['name'],
                file_type=request.POST['file_type'],
                folder=parent,
            )

            # request.session['folder_id'] = context['folder'].id
            # request.session['parent_id'] = context['parent'].id

            return redirect('folder', folder_id=parent.id)
        else :
            print("invalid form")
        return render(request, APPNAME + '/create_file.html', context)
    
    else :
        fileUploadForm = FileUploadForm()
        print(fileUploadForm)
        context['fileUploadForm'] = fileUploadForm

    return render(request, APPNAME + '/create_file.html', context)