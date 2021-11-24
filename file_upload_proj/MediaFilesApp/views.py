from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document

def file_upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    template_name='MediaFilesApp/uploadfile.html'
    context = {'form':form}
    return render(request,template_name,context)


def display_documents_view(request):
    documents_obj = Document.objects.all()
    template_name = 'MediaFilesApp/displayfiles.html'
    context = {'documents':documents_obj}
    return render(request,template_name,context)