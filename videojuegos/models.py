from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    plataforma = models.CharField(max_length=50)
    jugado = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.fecha_lanzamiento.year}) - {self.genero}"
    