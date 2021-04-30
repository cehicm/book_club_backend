from django.shortcuts import render
from django.views.generic import View
from apps.review.models import Review
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')

class ReviewListView(View):
    def get(self, request, *args, **kwargs):
        review_queryset = Review.objects.all()
        review_serializer = serializers.serialize('json', review_queryset)
        return HttpResponse(review_serializer, "application/json")

    def post(self,request):
        json_data = json.loads(request.body)
        from = ReviewForm(json_data)

        if form.is_valid():
            book = json_data("book") #?
            user = json_data("user")
            comment = json_data("comment")
            score = json_data("score")
            return JsonResponse(book,user,comment,score, status=200, safe=False)
        
        else:
            return JsonResponse("Form Invalid", status=400, safe=False)
