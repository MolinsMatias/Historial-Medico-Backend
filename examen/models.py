from django.db import models

# Create your models here.
from django.db import models

class Examen(models.Model):
    id_examen = models.BigIntegerField(primary_key=True)  # NUMBER(38), clave primaria
    fecha_examen = models.DateField()
    motivo = models.CharField(max_length=200)
    centro_medico = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    hist_medico_id_hist = models.BigIntegerField()  # o usar ForeignKey si está relacionada con otra tabla
    nombre_medico = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'EXAMENES'
        managed = False