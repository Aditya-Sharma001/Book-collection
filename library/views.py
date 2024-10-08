from django.shortcuts import render,  redirect, get_object_or_404
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.core.paginator import Paginator


def author_list(request):
    authors = Author.objects.all()
    # paginator = Paginator(authors,15)
    # page_number = request.GET
    return render(request,'library/author_list.html',{'authors':authors})

def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')

    else:
        form = AuthorForm()
    return render(request,'library/author_form.html',{'form':form})   

def author_edit(request, pk):
    author = get_object_or_404(Author,pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')

    else:
        form = AuthorForm(instance=author)
    return render(request,'library/author_form.html',{'form':form})  

def author_delete(request,pk):
    author = get_object_or_404(Author,pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request,'library/author_delete.html',{'author':author})

def book_list(request):
    books = Book.objects.all()
    return render(request,'library/book_list.html',{'books':books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'library/book_form.html',{'form':form})        

def book_edit(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request,'library/book_form.html',{'form':form})   

def book_delete(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request,'library/book_delete.html',{'books':book})     