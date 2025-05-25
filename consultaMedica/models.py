from django.db import models
from medico.models import Medico  # Asegúrate de que este import apunte al modelo correcto
from historialMedico.models import HistorialMedico  # Asegúrate de que este import sea correcto

class Consulta(models.Model):
    id_cons = models.BigAutoField(primary_key=True)  # NUMBER(38), NOT NULL, asumido como autoincremental
    fec_consulta = models.DateField()  # DATE, NOT NULL
    diagnostico = models.CharField(max_length=300)  # VARCHAR2(300), NOT NULL
    moti_consulta = models.CharField(max_length=200)  # VARCHAR2(200), NOT NULL
    eliminado = models.BooleanField()  # NUMBER, NOT NULL (se asume 0 o 1 como booleano)
    centro_med = models.CharField(max_length=100)  # VARCHAR2(100), NOT NULL
    observ = models.CharField(max_length=255)  # VARCHAR2(255), NOT NULL

    # Relaciones foráneas
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='MEDICO_ID_MED')
    historial_medico = models.ForeignKey(HistorialMedico, on_delete=models.CASCADE, db_column='HIST_MEDICO_ID_HIST')

    class Meta:
        db_table = 'CONSULTA_MEDICA'  # Nombre real de la tabla en la base de datos

    def __str__(self):
        return f'Consulta #{self.id_cons} - {self.fec_consulta}'
