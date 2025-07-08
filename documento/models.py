from django.db import models
from django.db.models import Max

class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=200, null=True, blank=True)
    nom_archivo = models.CharField(max_length=200, null=True, blank=True)
    fecha_carga = models.DateField()
    tamanio_archivo = models.CharField(max_length=500, null=True, blank=True)
    id_paciente = models.BigIntegerField()
    eliminado = models.BooleanField()
    hist_medico_id_hist = models.BigIntegerField()

    class Meta:
        db_table = 'DOCUMENTO'
        managed = False  # la tabla ya existe, no la gestiona Django

    def save(self, *args, **kwargs):
        if self.id_documento is None:
            ultimo_id = Documento.objects.aggregate(Max('id_documento'))['id_documento__max']
            self.id_documento = (ultimo_id or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Documento #{self.id_documento} - Paciente {self.id_paciente}'
