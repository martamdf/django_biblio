from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from biblio.forms import BookForm, CategoryForm
from biblio.models import Book, Category
from django.views.generic.edit import DeleteView
from django.utils import timezone
from .filters import BookFilter


def index(request):
    return HttpResponse("Hello, world. You're at the biblio index.")

#Libros

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'categoria']

class HomeView(ListView):
    model = Book
    paginate_by = 100  # si queremos paginación

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'biblio/book_detail.html'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        print(context)
        print(type(context['object']))
        return context

class BooksUpdateView(UpdateView):
    model = Book
    fields = [
        "title",
        "author",
        "categoria"
    ]
    success_url ="/"

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('home')


#Categorías

class CategoryCreateView(CreateView):
    model = Category
    fields = ['category_name']

class CategoryListView(ListView):
    model = Category
    paginate_by = 100  # paginación

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'biblio/category_detail.html'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    fields = [
        "category_name",
    ]
    success_url = reverse_lazy('categories')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')

#TODO:Filtros
def search(request):
    book_list = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    return render(request, 'biblio/busqueda.html', {'filter': book_filter})