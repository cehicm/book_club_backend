from django.shortcuts import render
import json
from django.views.generic import View
from apps.book.models import Book
from apps.book.forms import BookForm
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class BookListView(View):
    def get(self, request, *args, **kwargs):
        book_queryset = Book.objects.all()
        books_serialized = serializers.serialize('json', book_queryset)
        return HttpResponse(books_serialized, content_type="application/json") #isto kao JsonResponse, drugacija forma

    def post(self, request):
        json_data = json.loads(request.body)

        form = BookForm(json_data)
        
        if form.is_valid():
            name = json_data["name"]
            # save model in base
            return JsonResponse(name, status=200, safe=False) #status=200 - status oke, safe=False - po definiciji DJAngo ih vidi kao unsafe, mora da se degnise
        else:
            return JsonResponse("Form invalid", status=400, safe=False) #status=200 - status oke, safe=False - po definiciji DJAngo ih vidi kao unsafe, mora da se degnise

