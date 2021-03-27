from django.contrib import admin

from apps.book.models import Book


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)

# Register your models here.
