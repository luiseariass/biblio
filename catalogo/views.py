from django.shortcuts import render, redirect
from django.views import generic
from catalogo.models import Book, Author, Genre, Format
import django_filters
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):

    num_books = Book.objects.all().count()
    books = Book.objects.all()
    myFilter = BookFilter()
    if request.method == 'POST':
        print("entre aqui")
        myFilter = BookFilter(request.POST, queryset=books)
        if myFilter.form.is_valid():
            title = request.POST.get('title', False)
            author = request.POST.get('author__name', False)
            format= request.POST.get('format', False)
            url = f"http://127.0.0.1:8000/catalogo/books/?title={title}&author__name={author}&format={format}"
            print(url)
            return redirect(url)

    context = {
        'num_books': num_books,
        'books': books,
        'myFilter': myFilter,
    }
    return render(request, 'index.html', context=context)


class BookDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Book


class AuthorFilter(LoginRequiredMixin,django_filters.FilterSet):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    name = django_filters.CharFilter(label='Nombre', lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ['name']

@login_required
def author_list(request):
    authors = Author.objects.all()
    filtroautor = AuthorFilter(request.GET, queryset=authors)
    authors = filtroautor.qs
    context = {'filtroautor': filtroautor, 'authors': authors}
    return render(request, 'catalogo/author_list2.html', context)


class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Author


class BookFilter(LoginRequiredMixin,django_filters.FilterSet):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    title = django_filters.CharFilter(label='Título', lookup_expr='icontains')
    author__name = django_filters.CharFilter(label='Autor', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author__name', 'format']

@login_required
def book_list(request):
    print('entre a book_list')
    books = Book.objects.all()
    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    context = {'myFilter': myFilter, 'books': books}
    return render(request, 'catalogo/book_list2.html', context)


