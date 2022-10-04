from tabnanny import verbose
from django.db import models

# Create your models here.
class Work(models.Model):
    title=models.CharField(max_length=50, verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    image=models.ImageField(verbose_name="Imagen", upload_to="portfolios")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name="portfolio"
        verbose_name_plural="portfolios"
        ordering=['-created']
        
    def __str__(self):
        return self.title