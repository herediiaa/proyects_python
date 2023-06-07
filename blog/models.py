from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo= models.CharField(max_length=100,default='')
    autor=models.CharField(max_length=50,default='')
    contenido= models.TextField(max_length=1000,default='')

    def __str__(self) -> str:
        return self.titulo