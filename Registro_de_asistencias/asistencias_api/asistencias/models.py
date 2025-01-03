from django.db import models
from django.core.exceptions import ValidationError

class Asistencia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del empleado")
    fecha = models.DateField(verbose_name="Fecha de asistencia")
    hora_entrada = models.TimeField(null=True, blank=True, verbose_name="Hora de entrada")
    hora_salida = models.TimeField(null=True, blank=True, verbose_name="Hora de salida")
    observaciones = models.TextField(null=True, blank=True, verbose_name="Observaciones")

    def clean(self):
        # Validar que al menos una hora (entrada o salida) esté registrada
        if not self.hora_entrada and not self.hora_salida:
            raise ValidationError("Debe registrar al menos la hora de entrada o la hora de salida.")
        
        # Validar que la hora de salida sea posterior a la hora de entrada
        if self.hora_entrada and self.hora_salida and self.hora_salida <= self.hora_entrada:
            raise ValidationError("La hora de salida debe ser posterior a la hora de entrada.")
    
    def save(self, *args, **kwargs):
        self.clean()  # Llamar al método clean para validar antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        observaciones_texto = f" - Observaciones: {self.observaciones}" if self.observaciones else ""
        return (
            f"{self.nombre} - {self.fecha} - "
            f"Entrada: {self.hora_entrada or 'No registrada'} - "
            f"Salida: {self.hora_salida or 'No registrada'}{observaciones_texto}"
        )
