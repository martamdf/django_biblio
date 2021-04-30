from django.contrib import admin
from django.urls import path, include
from biblio import views
from biblio.views import HomeView, BooksUpdateView, BookDeleteView, BookDetailView, BookCreateView, CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('biblio/', include('biblio.urls')),
    
    #Home
    path('', HomeView.as_view(), name='home'),

    #Books
    path('biblio/new/', BookCreateView.as_view(), name='book-add'),
    path('biblio/<int:pk>/update', BooksUpdateView.as_view(), name='book_form'),
    path('biblio/<int:pk>/book_confirm_delete', BookDeleteView.as_view(), name='book_confirm_delete'),
    path('biblio/<int:pk>/book_detail', BookDetailView.as_view(), name='book_detail'),

    #Categories
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('biblio/new_category/', CategoryCreateView.as_view(), name='category_form'),
    path('biblio/<int:pk>/category_update', CategoryUpdateView.as_view(), name='category_update'),
    path('biblio/<int:pk>/category_confirm_delete', CategoryDeleteView.as_view(), name='category_confirm_delete'),
    path('biblio/<int:pk>/category_detail', CategoryDetailView.as_view(), name='category_detail'),

    #Búsqueda

]
