from django.db import models
from medico.models import Medico  # Asegúrate de que este import apunte al modelo correcto


class LogAuditoria(models.Model):
    id_log = models.IntegerField(primary_key=True)
    fecha_suceso = models.DateTimeField()
    operacion = models.CharField(max_length=100)
    id_usuario = models.IntegerField()  # Sin ForeignKey

    class Meta:
        db_table = 'LOG_AUDITORIA'

    def __str__(self):
        return f"{self.fecha_suceso} - {self.operacion}"

    @property
    def medico(self):
        from medico.models import Medico
        try:
            return Medico.objects.get(pk=self.id_usuario)
        except Medico.DoesNotExist:
            return None

