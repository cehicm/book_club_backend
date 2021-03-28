from django.shortcuts import render
from django.views.generic import View
from apps.book.models import Book
from django.core import serializers
from django.http import HttpResponse
# Create your views here.


class BookListView(View):
    def get(self, request, *args, **kwargs):
        book_queryset = Book.objects.all()
        books_serialized = serializers.serialize('json', book_queryset)
        return HttpResponse(books_serialized, content_type="application/json")
