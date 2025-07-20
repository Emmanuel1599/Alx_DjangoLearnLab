import sys
import os
import django

# Add the base directory of your project to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

if __name__ == "__main__":
    print("Books by Author:")
    for book in get_books_by_author("Chinua Achebe"):
        print(book)

    print("\nBooks in Library:")
    for book in list_books_in_library("Accra Central Library"):
        print(book)

    print("\nLibrarian for Library:")
    print(get_librarian_for_library("Accra Central Library"))
