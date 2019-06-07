from django.db import models

class Medicamento(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    fecha_ven = models.DateField()
    descripcion = models.TextField()

class Paciente (models.Model):
    cedula = models.CharField(max_length=11)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    fecha_registro = models.DateTimeField(auto_now_add=True)


