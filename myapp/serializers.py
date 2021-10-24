import os

from rest_framework import serializers

from . import models


class VehicleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VehicleModel
        fields = '__all__'


class VehicleManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VehicleManufacturer
        fields = '__all__'


class VehicleModelImageSerializer(serializers.ModelSerializer):
    image_file_name = serializers.SerializerMethodField()

    class Meta:
        model = models.VehicleModelImage
        fields = '__all__'

    def get_image_file_name(self, obj):
        return os.path.basename(obj.image.name)
