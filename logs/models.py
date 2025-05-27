from django.db import models
from django.db.models import Max

class LogAuditoria(models.Model):
    id_log = models.AutoField(primary_key=True)
    fecha_suceso = models.DateTimeField()
    operacion = models.CharField(max_length=100)
    id_usuario = models.IntegerField()  

    class Meta:
        db_table = 'LOG_AUDITORIA'

    def save(self, *args, **kwargs):
        if self.id_log is None:
            ultimo_id = LogAuditoria.objects.aggregate(Max('id_log'))['id_log__max']
            self.id_log = (ultimo_id or 0) + 1
        super().save(*args, **kwargs)
