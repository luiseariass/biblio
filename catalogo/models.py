from django.db import models
from django.urls import reverse
from gdstorage.storage import GoogleDriveStorage


gd_storage = GoogleDriveStorage()


class Genre(models.Model):
    """Model representing a book genre."""

    name = models.CharField(max_length=200, help_text='Escriba el género del libro (ej. Ciencia Ficción)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Format(models.Model):

    name = models.CharField(max_length=200, help_text="Ingrese el formato del archivo del libro")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Seleccione el genero dellibro')
    format = models.ForeignKey('Format', on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='files', storage=gd_storage, null= True)

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):

    """Model representing an author."""

    name = models.CharField(max_length=100)
    biografia = models.TextField(max_length=1000, help_text='Ingrese la biografía del autor',null= True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name
