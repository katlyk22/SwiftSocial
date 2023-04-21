from django.db import models

class Post(models.Model):
    carousel_caption_title = models.CharField(max_length=50)
    carousel_caption_description = models.CharField(max_length=100)
    heading = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
   
    def __str__(self):
       return f" {self.id} -- {self.carousel_caption_title} -- {self.heading} "


class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    apodo = models.TextField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido}"