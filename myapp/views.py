from django.shortcuts import get_object_or_404, render
from .models import VehicleManufacturer, VehicleModel, VehicleModelImage
from django.http import JsonResponse
from django.core.serializers import serialize


def home(request):
    context = dict()
    vehicle_manufacturers = VehicleManufacturer.objects.all()
    context['vehicle_manufacturers'] = vehicle_manufacturers
    return render(request, template_name='myapp/home.html', context=context)

