from django.db import models

class Receta(models.Model):
    id_rece = models.BigIntegerField(primary_key=True)  # NUMBER(38), clave primaria
    fecha_creacion = models.DateField()                # DATE
    est_receta = models.IntegerField()                  # NUMBER
    consulta_medica_id_cons = models.BigIntegerField()  # NUMBER(38)

    class Meta:
        db_table = 'RECETA' 
        managed = False

