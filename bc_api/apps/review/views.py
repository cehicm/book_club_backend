from django.shortcuts import render
from django.views.generic import View
from apps.review.models import Review
from django.core import serializers
from django.http import HttpResponse


class ReviewListView(View):
    def get(self, request, *args, **kwargs):
        review_queryset = Review.objects.all()
        review_serializer = serializers.serialize('json', review_queryset)
        return HttpResponse(review_serializer, "application/json")
