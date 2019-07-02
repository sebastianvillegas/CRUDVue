from rest_framework import serializers
from .models import Medicamento, Paciente

class MedicamentoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ('id','codigo','nombre','fecha_ven','descripcion')

class PacienteSerialize(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('cedula','medicamento','nombre','fecha_registro', 'nombreMedicamento')


