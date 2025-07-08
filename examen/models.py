from django.db import models
from django.db.models import Max

class Examen(models.Model):
    id_examen = models.AutoField(primary_key=True)  # NUMBER(38)
    fecha_examen = models.DateField()
    motivo = models.CharField(max_length=200)
    centro_medico = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    hist_medico_id_hist = models.BigIntegerField()  # puedes cambiarlo a ForeignKey si corresponde
    nombre_medico = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'EXAMENES'
        managed = False  # la tabla ya existe

    def save(self, *args, **kwargs):
        if self.id_examen is None:
            ultimo_id = Examen.objects.aggregate(Max('id_examen'))['id_examen__max']
            self.id_examen = (ultimo_id or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Examen #{self.id_examen} - {self.fecha_examen}'
