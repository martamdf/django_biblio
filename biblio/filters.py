from biblio.models import Book, Category
import django_filters

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'categoria', ]