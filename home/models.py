from django.db import models
from django.utils import timezone
from tensorflow.keras.preprocessing import image


# Create your models here.
class feedback(models.Model):
    U_name = models.CharField(max_length=200)
    email = models.CharField(max_length=30)
    phoneno = models.CharField(max_length=10)
    message = models.CharField(max_length=200)

    def __str_(self):
        return self.U_name
    

# Create your models here.
class UploadImage(models.Model):
    image =models.ImageField()