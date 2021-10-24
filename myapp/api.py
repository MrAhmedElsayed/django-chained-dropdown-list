from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from .models import VehicleManufacturer, VehicleModel, VehicleModelImage


@api_view(['GET'])
def vehicle_models_view(request):
    if request.GET.get("operation") == "vehicle_manufacturer_select" and request.is_ajax():
        vehicle_manufacturer_id = request.GET.get("vehicle_manufacturer_selector_id", None)
        vehicle_manufacturer = get_object_or_404(VehicleManufacturer, id=vehicle_manufacturer_id)
        vehicle_models = VehicleModel.objects.filter(vehicle_manufacturer=vehicle_manufacturer)
        vehicle_models_serializer = serializers.VehicleManufacturerSerializer(vehicle_models, many=True)
        return Response(vehicle_models_serializer.data)


@api_view(['GET'])
def vehicle_images_view(request):
    if request.GET.get("operation") == "vehicle_model_select" and request.is_ajax():
        vehicle_model_id = request.GET.get("vehicle_model_selector_id", None)
        vehicle_model = get_object_or_404(VehicleModel, id=vehicle_model_id)
        vehicle_images = VehicleModelImage.objects.filter(vehicle_model=vehicle_model)
        vehicle_images_serializer = serializers.VehicleModelImageSerializer(vehicle_images, many=True)
        return Response(vehicle_images_serializer.data)

# @api_view(['GET','POST'])
# def students_list(request):
#     if request.method == 'GET':
#         students = Students.objects.all()
#         serializers = StudentSerializers(students,many=True)
#         return Response(serializers.data)
#
#     elif(request.method == 'POST'):
#         serializers = StudentSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
