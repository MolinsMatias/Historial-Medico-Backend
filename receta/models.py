from django.db import models
from django.db.models import Max


class Medicamento(models.Model):
    id_medica = models.BigAutoField(primary_key=True, db_column='ID_MEDICA')
    nom_medica = models.CharField(max_length=100, db_column='NOM_MEDICA')
    descripcion = models.CharField(max_length=100, null=True, blank=True, db_column='DESCRIPCION')

    class Meta:
        db_table = 'MEDICAMENTO'
        managed = False


class Receta(models.Model):
    id_rece = models.AutoField(primary_key=True)  # NUMBER(38), clave primaria
    fecha_creacion = models.DateField()                # DATE
    est_receta = models.IntegerField()                  # NUMBER
    consulta_medica_id_cons = models.BigIntegerField()  # NUMBER(38)

    class Meta:
        db_table = 'RECETA' 
        managed = False
    def save(self, *args, **kwargs):
            if self.id_rece is None:
                ultimo_id = Receta.objects.aggregate(Max('id_rece'))['id_rece__max']
                self.id_rece = (ultimo_id or 0) + 1
            super().save(*args, **kwargs)                  

class DetalleReceta(models.Model):
    id_det = models.AutoField(primary_key=True)  # NUMBER(38), clave primaria
    descripcion = models.CharField(max_length=350)     # VARCHAR2(350)
    frecuencia = models.CharField(max_length=200)      # VARCHAR2(200)
    cant_preescrita = models.IntegerField()            # NUMBER(10)
    receta_id_rece = models.ForeignKey(Receta, on_delete=models.CASCADE, db_column='receta_id_rece')   # NUMBER(38), FK a MEDICAMENTO
    medicamento_id_medica = models.ForeignKey(Medicamento, on_delete=models.CASCADE, db_column='medicamento_id_medica')   # NUMBER(38), FK a MEDICAMENTO

    class Meta:
        db_table = 'DETALLE_RECETA'
        managed = False  # Cambiar a True si Django debe manejar la tabla
    def save(self, *args, **kwargs):
            if self.id_det is None:
                ultimo_id = DetalleReceta.objects.aggregate(Max('id_det'))['id_det__max']
                self.id_det = (ultimo_id or 0) + 1
            super().save(*args, **kwargs)          
