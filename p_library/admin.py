from django.contrib import admin
from p_library.models import Book, Author, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publisher')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass