from django.db import models

class LogAuditoria(models.Model):
    id_log = models.IntegerField(primary_key=True)
    fecha_suceso = models.DateTimeField()
    operacion = models.CharField(max_length=100)
    id_usuario = models.IntegerField()

    class Meta:
        db_table = 'LOG_AUDITORIA'  # Muy importante: usar el nombre real de la tabla en la BD

    def __str__(self):
        return f"{self.fecha_suceso} - {self.operacion}"
