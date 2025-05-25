from django.db import models

class Medico(models.Model):
    id_med = models.BigAutoField(primary_key=True)  # NUMBER(38), NOT NULL, asumido autoincremental
    rut = models.CharField(max_length=10)  # VARCHAR2(10), NOT NULL
    nombre = models.CharField(max_length=100)  # VARCHAR2(100), NOT NULL
    apellido = models.CharField(max_length=100)  # VARCHAR2(100), NOT NULL
    email = models.CharField(max_length=200)  # VARCHAR2(200), NOT NULL
    est_med = models.IntegerField()  # NUMBER, NOT NULL (estado del médico, posiblemente 0 o 1)



    class Meta:
        db_table = 'MEDICO'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
