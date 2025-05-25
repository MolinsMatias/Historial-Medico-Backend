from django.db import models
from paciente.models import Paciente
from medico.models import Medico  # Asegúrate de que este import apunte al modelo correcto

class HistorialMedico(models.Model):
    id_hist = models.BigAutoField(primary_key=True)  # NUMBER(38) con NOT NULL, asumido como autoincremental
    fec_creacion = models.DateField()  # DATE
    est_visib = models.IntegerField()  # NUMBER
    observ = models.CharField(max_length=500)  # VARCHAR2(500)
    
    paciente_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='PACIENTE_MEDICO_ID_MED')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='PACIENTE_ID_PAC')


    class Meta:
        db_table = 'HIST_MEDICO'  # Puedes cambiarlo al nombre real si es distinto

    def __str__(self):
        return f'Historial #{self.id_hist} - Paciente {self.paciente_id}'