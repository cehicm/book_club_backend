from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from apps.user.models import BCUser
from django.core import serializers
from django.http import HttpResponse


class BCUserListView(View):
    def get(self, request, *args, **kwargs):
        bcuser_queryset = BCUser.objects.all()
        bcuser_serialized = serializers.serialize('json', bcuser_queryset)
        return HttpResponse(bcuser_serialized, content_type="application/json")
