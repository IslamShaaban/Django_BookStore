from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
#Index Function to get All Books
@login_required
@permission_required(['books.view_book'], raise_exception=True)
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books' : books
    })

#Create Function to Create New Book
@login_required
@permission_required(['books.view_book'], raise_exception=True)
def create(request):
    bookForm = BookForm(request.POST or None)
    if bookForm.is_valid():
        bookForm.save()
        return redirect('index')
    else:
        return render(request, 'books/create.html', {
            'form' : bookForm
        })
        
#Edit Function to Edit Certain Book
@login_required
def edit(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'books/edit.html', {
        'form' : form,
        'book' : book
    })

#Delete Function to Delete Certain Book
@login_required
def delete(request, id): 
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('index')