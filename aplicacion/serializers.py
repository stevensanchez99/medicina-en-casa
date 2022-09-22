from rest_framework import serializers
from .models import  Familiar, Historia_clinica, Paciente, Personal_medico, Signos_vitales

#django a json
#cada clase tiene el mismo ombre de la tabla creada + el Serializer
#se le indica que muestre todos los campos __all__ para rellenarlos.

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields='__all__' #traer todo

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Familiar
        fields='__all__' #traer todo

class Historia_clinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Historia_clinica
        fields='__all__' #traer todo

class Personal_medicoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personal_medico
        fields='__all__' #traer todo
        
class Signos_vitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Signos_vitales
        fields='__all__' #traer todo

        