from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, Format

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Format)


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = [('name', 'biografia')]
    inlines = [BooksInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'format', 'file')
    filter_vertical = ('genre', 'genre')


