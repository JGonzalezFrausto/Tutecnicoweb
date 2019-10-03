from django.db import models

# Create your models here.
class Tecnico(models.Model):  #Auto(models.Model):

  nombre = models.CharField(max_length=300)
  servicio = models.CharField(max_length=300)
  telefono = models.CharField(max_length=300)
  email = models.CharField(max_length=300)
  direccion = models.CharField(max_length=300)
  image = models.ImageField(upload_to='auto_images',
                            default='media/default.png')


#  nombre = models.CharField(max_length=100)
#  valor = models.DecimalField(max_digits=10, decimal_places=2)
 # km = models.CharField(max_length=100)
 # modelo = models.CharField(max_length=100)
  #color = models.CharField(max_length=100)
  #localizacion = models.CharField(max_length=100)
  #img_url = models.CharField(max_length=100)
  #image = models.ImageField(upload_to='auto_images',
  #                          default='media/default.png')

  def __str__(self):
    return self.nombre