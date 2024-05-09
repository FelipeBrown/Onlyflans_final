import uuid
from django import forms
from django.db import models
from django.utils.text import slugify


# Create your models here.


class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, blank=False)
    descripcion = models.TextField(blank=False, null=False)
    imagen = models.URLField(blank=False)
    slug = models.SlugField(unique=True, max_length=255,blank=True)
    is_private = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=10 ,decimal_places=3, default=500)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)    
        
    def __str__(self):
        return self.name
    

class Contacto(models.Model):
  contactForm_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  customer_name = models.CharField(max_length=50, blank=False)
  customer_email = models.EmailField(blank=False)
  message = models.TextField(blank=False)
  
  def __str__(self):
        return self.customer_name
    

class CalificacionFlan(models.Model):
    flan = models.ForeignKey(Flan, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=((1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')))

    def __str__(self):
        return f"{self.flan.name} - {self.calificacion} estrellas"
        