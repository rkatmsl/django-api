from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users

def index(request):
    return HttpResponse("Hello Geeks")

@csrf_exempt
def store(request, device_id):
    try:
        visitor = Users.objects.get(device_id=device_id)
        return JsonResponse({'exists': True})
    except Users.DoesNotExist:
        new_visitor = Users.objects.create(device_id=device_id)
        return JsonResponse({'exists': False})  
