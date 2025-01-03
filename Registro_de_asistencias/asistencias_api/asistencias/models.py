from django.db import models

class Asistencia(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.fecha} - {'Presente' if self.presente else 'Ausente'}"
