from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Medicamento, Paciente
from .serializers import MedicamentoSerialize, PacienteSerialize

# Create your views here.

class MedicamentoAPI(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerialize

class PacienteAPI(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerialize