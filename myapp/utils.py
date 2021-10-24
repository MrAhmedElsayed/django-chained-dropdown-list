from myproject.settings import MEDIA_URL


def vehicle_model_image_url(instance, filename):
	
	""" example: uploads/bmw_manufacturer/c class-model/car.jpg """

	return '{0}/{1}_manufacturer/{2}_model/{3}'.format(
		MEDIA_URL, 
		instance.vehicle_model.vehicle_manufacturer.name, 
		instance.vehicle_model.name, 
		filename
	)
