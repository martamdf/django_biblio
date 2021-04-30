from django.forms import ModelForm
from biblio.models import Book, Category
from django.core.exceptions import ValidationError

class BookForm(ModelForm):
    #Formulario para el modelo Libro
    class Meta:
        model = Book
        exclude = ['id', 'cover']

class CategoryForm(ModelForm):
    #Formulario para el modelo Categoría
    class Meta:
        model = Category
        exclude = ['id']