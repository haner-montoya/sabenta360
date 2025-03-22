from django.db import models
from core.types.categorias import Categorias
from core.types.socialmedia import Social_Media

def subir_logo(instance, file_name):
    return 'img/comercios/' + file_name

# Create your models here.
class Comercio(models.Model):
    nombre_comercio = models.CharField(max_length=255)
    categoria = models.CharField(choices = Categorias, max_length=45)
    direccion = models.TextField()
    telefono = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    imagen = models.ImageField(upload_to=subir_logo)

    class Meta:
        verbose_name = 'Comercio'

    def __str__(self):
        return f'{self.nombre_comercio}'


class SocialMedia(models.Model):
    comercio = models.ForeignKey(Comercio, on_delete = models.CASCADE)
    social_media = models.CharField(choices = Social_Media, max_length=200)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return f'{self.comercio} - {self.social_media}'
