from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

# Create your views here.

#Index Function to get All Books
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books' : books
    })

#Create Function to Create New Book
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
def delete(request, id): 
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('index')