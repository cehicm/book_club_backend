from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from apps.user.models import BCUser
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class BCUserListView(View):
    def get(self, request, *args, **kwargs):
        bcuser_queryset = BCUser.objects.all()
        bcuser_serialized = serializers.serialize('json', bcuser_queryset)
        return HttpResponse(bcuser_serialized, content_type="application/json")

    def post(self,request):
        json_data = json.loads(request.body)

        form = BookFrom(json_data)

        if form.is_valid():
            user = json_data["user"]
            return JsonResponse(user, status=200, safe=False)
        else:
            return JsonResponse("Form Invalid", status=400, safe=False)