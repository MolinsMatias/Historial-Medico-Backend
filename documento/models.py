from django.db import models

class Documento(models.Model):
    id_documento = models.BigIntegerField(primary_key=True)
    tipo_documento = models.CharField(max_length=200, null=True, blank=True)
    nom_archivo = models.CharField(max_length=200, null=True, blank=True)
    fecha_carga = models.DateField()
    tamanio_archivo = models.CharField(max_length=500, null=True, blank=True)
    id_paciente = models.BigIntegerField()
    eliminado = models.BooleanField()
    hist_medico_id_hist = models.BigIntegerField()

    class Meta:
        db_table = 'DOCUMENTO'
        managed = False  # ya que la tabla existe en la base de datos

