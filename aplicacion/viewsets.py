#API REST 
from rest_framework import viewsets

from . import models
from . import serializers


#vistas
#cada clase tiene el mismo ombre de la tabla creada + el Viewset que hace referecia al archivo de las vistas

class PacienteViewset(viewsets.ModelViewSet):
    queryset=models.Paciente.objects.all() #consulta de todos los objetos de la table
    serializer_class=serializers.PacienteSerializer #se llama cada serializer del archivo serializer

class FamiliarViewset(viewsets.ModelViewSet):
    queryset=models.Familiar.objects.all() #consulta de todos los objetos de la table
    serializer_class=serializers.FamiliarSerializer

class Historia_clinicaViewset(viewsets.ModelViewSet):
    queryset=models.Historia_clinica.objects.all() #consulta de todos los objetos de la table
    serializer_class=serializers.Historia_clinicaSerializer 


class Personal_medicoViewset(viewsets.ModelViewSet):
    queryset=models.Personal_medico.objects.all() #consulta de todos los objetos de la table
    serializer_class=serializers.Personal_medicoSerializer 

class Signos_vitalesViewset(viewsets.ModelViewSet):
    queryset=models.Signos_vitales.objects.all() #consulta de todos los objetos de la table
    serializer_class=serializers.Signos_vitalesSerializer 

    


