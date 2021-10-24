from django.db import models
from .utils import vehicle_model_image_url

# source of cars example: https://www.carmodelslist.com/audi/


class VehicleManufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class VehicleModel(models.Model):
    name = models.CharField(max_length=50)
    vehicle_manufacturer = models.ForeignKey(to=VehicleManufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.vehicle_manufacturer.name}"


class VehicleModelImage(models.Model):
    image = models.ImageField(upload_to=vehicle_model_image_url)
    vehicle_model = models.ForeignKey(to=VehicleModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"image - {self.vehicle_model.name} - {self.vehicle_model.vehicle_manufacturer.name}"
