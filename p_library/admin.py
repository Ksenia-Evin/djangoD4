from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, UserProfile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass
  
# Register your models here.  
@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass