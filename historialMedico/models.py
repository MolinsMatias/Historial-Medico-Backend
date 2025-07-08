from django.db import models
from paciente.models import Paciente
from medico.models import Medico 
from django.db.models import Max

class HistorialMedico(models.Model):
    id_hist = models.AutoField(primary_key=True)
    fec_creacion = models.DateField()
    est_visib = models.IntegerField()
    observ = models.CharField(max_length=500)

    paciente_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='PACIENTE_MEDICO_ID_MED')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='PACIENTE_ID_PAC')

    class Meta:
        db_table = 'HIST_MEDICO'

    def __str__(self):
        return f'Historial #{self.id_hist} - Paciente {self.paciente_id}'

    def save(self, *args, **kwargs):
        if self.id_hist is None:
            ultimo_id = HistorialMedico.objects.aggregate(Max('id_hist'))['id_hist__max']
            self.id_hist = (ultimo_id or 0) + 1
        super().save(*args, **kwargs)
