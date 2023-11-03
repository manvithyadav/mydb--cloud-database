from django.shortcuts import render, redirect
from django.template.defaulttags import register

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


@register.filter
def formatDateTime(upload_time) :
    return upload_time.strftime("%m/%d/%Y, %H:%M:%S")

@register.filter
def isTrashFolder(request, folder_id) :
    # print(request, folder_id, request.user.dbuser.trash_id, type(request.user.dbuser.trash_id), type(folder_id))
    return str(request.user.dbuser.trash_id) == str(folder_id)


def renderFolderView(request, folder_id) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    if request.user.is_superuser :
       return redirect('home')
    
    context = {}

    try :
        folder = Folder.objects.get(id=folder_id)

        parent = folder.parent
        
        parents = []
        
        while parent is not None :
            parents.append(parent)
            parent = parent.parent

        parents.reverse()

        context['parents'] = parents
        context['folder'] = folder

        children = folder.folder_set.all()
        context['children'] = children

        files = folder.file_set.all()
        context['files'] = files
        for file in files :
            if file.file :
                print(file.upload_time.strftime("%m/%d/%Y, %H:%M:%S"))

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

    parents = []


    # if we use 'parent' for iterating param, it will be confusing
    # for folder view, parent is not current folder
    # while for create folder and upload file view the parent is same ad the current folder
    # so we start with parent's parent here and in upload file view
    par = parent.parent
    while par is not None :
        parents.append(par)
        par = par.parent

    parents.reverse()

    context['parents'] = parents



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

    parents = []

    par = parent.parent
    while par is not None :
        parents.append(par)
        par = par.parent

    parents.reverse()

    context['parents'] = parents


    if request.method == 'POST' :
        fileUploadForm = FileUploadForm(request.POST, request.FILES)
        if fileUploadForm.is_valid() :
            # create a file
            # store folder_id and parent_id in session
            # redirect to folder

            print(f'{request.FILES}')

            file = File.objects.create(
                user=request.user,
                name=request.POST['name'],
                file_type=request.POST['file_type'],
                folder=parent,
                file=request.FILES['file'],
            )

            # request.session['folder_id'] = context['folder'].id
            # request.session['parent_id'] = context['parent'].id

            return redirect('folder', folder_id=parent.id)
        else :
            print("invalid form")
            print(fileUploadForm.errors)
        return render(request, APPNAME + '/create_file.html', context)
    
    else :
        fileUploadForm = FileUploadForm()
        # print(fileUploadForm)
        context['fileUploadForm'] = fileUploadForm

    return render(request, APPNAME + '/create_file.html', context)


def renderDeleteFileView(request, parent_id, file_id) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    if request.user.is_superuser :
       return redirect('home')
    
    context = {}

    
    try :
        # create a file in user's trash folder
        file = File.objects.get(id=file_id)

        # if current folder is trash, then we don't create a file again in trash
        if request.user.dbuser.trash_id != parent_id :

            trash = Folder.objects.get(id=request.user.dbuser.trash_id)
            new_file = File.objects.create(
                user=request.user,
                name=file.name,
                file_type=file.file_type,
                folder=trash,
                file=file.file,
                restore_folder_id=parent_id,
            )
            new_file.save()

        file.delete()

        

        return redirect('folder', folder_id=parent_id)
    
    except File.DoesNotExist :
        print("file not found")
        return redirect('home')
    
    # return render(request, APPNAME + '/delete_file.html', context)


def renderRestoreFileView(request, parent_id, file_id) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    if request.user.is_superuser :
       return redirect('home')
    
    context = {}

    try :
        # create a file in user's trash folder
        file = File.objects.get(id=file_id)
        
        file.folder = Folder.objects.get(id=file.restore_folder_id)
        file.restore_folder_id = None
        file.save()

        

        return redirect('folder', folder_id=parent_id)
    
    except File.DoesNotExist :
        print("file not found")
        return redirect('home')