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
    mapa = models.URLField(max_length=500, null=True)
    publicado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Comercio'

    def __str__(self):
        return f'{self.nombre_comercio}'


class SocialMedia(models.Model):
    comercio = models.ForeignKey(Comercio, on_delete = models.CASCADE)
    social_media = models.CharField(choices = Social_Media, max_length=200)
    url = models.URLField(max_length=200, null=True)
    estado = models.BooleanField(default=True, verbose_name='¿Activo?')

    class Meta:
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return f'{self.comercio} - {self.social_media}'
