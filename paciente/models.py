from django.db import models

class Paciente(models.Model):
    id_pac = models.BigIntegerField(primary_key=True)
    sexo = models.BooleanField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    alergias = models.CharField(max_length=100)
    seguro_medico = models.CharField(max_length=100, blank=True, null=True)
    obser_clinica = models.CharField(max_length=350)
    
    class Meta:
        db_table = 'PACIENTE'
        managed = False  
