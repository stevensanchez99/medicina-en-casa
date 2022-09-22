from django.db import models

# Create your models here.
#clase nombre tabal
#creacio de bases de datos.


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombres =models.CharField('nombres',max_length=45, null=False,blank=False)
    apellidos =models.CharField('apellidos',max_length=45, null=True,blank=True)
    genero = models.CharField('genero',max_length=45,default="Some String")# Nuevo
    tipo_documento =models.CharField('tipo de documento',max_length=45, null=True,blank=True)
    numero_documento =models.CharField('numero de documento',max_length=45, null=False,blank=False)
    email =models.EmailField('email',max_length=45, null=False,blank=False)
    telefono =models.CharField('telefono',max_length=45, null=False,blank=False)
    direccion =models.CharField('direccion',max_length=45, null=False,blank=False)
    ciudad = models.CharField('ciudad',max_length=45,default="Some String")#nuevo
    #Familiar_paciente = models.ForeignKey(Familiar,  on_delete=models.CASCADE)
   # Personal_medico = models.ForeignKey(Personal_medico, on_delete=models.CASCADE)


class Familiar(models.Model):
    id_Familiar=models.AutoField(primary_key=True)
    nombres =models.CharField('nombres',max_length=45, null=False,blank=False)
    apellidos =models.CharField('apellidos',max_length=45, null=True,blank=True)
    tipo_documento =models.CharField('tipo de documento',max_length=45, null=True,blank=True)
    numero_documento =models.CharField('numero de documento',max_length=45, null=False,blank=False)
    genero = models.CharField('genero',max_length=45,default="Some String")# Nuevo
    parentesco = models.CharField('parentesco',max_length=45)# Nuevo
    email =models.EmailField('email',max_length=45, null=False,blank=False)
    telefono =models.CharField('telefono',max_length=45, null=False,blank=False)
    direccion =models.CharField('direccion',max_length=45, null=False,blank=False)
    

class Historia_clinica(models.Model):
    id_historia=models.AutoField(primary_key=True)
    fecha_registro = models.DateField('fecha_registro',auto_now=False,auto_now_add=True)
    fecha_consulta = models.DateField()#nuevo
    recomenacion_medica = models.TextField()
    paciente = models.ForeignKey(Paciente, related_name='historia_clinica', on_delete=models.CASCADE)


class Personal_medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombres =models.CharField('nombres',max_length=45, null=False,blank=False)
    apellidos =models.CharField('apellidos',max_length=45, null=True,blank=True)
    genero = models.CharField('genero',max_length=45)# Nuevo
    tipo_documento =models.CharField('tip de documento',max_length=45, null=True,blank=True)
    numero_documento =models.CharField('numero de documento',max_length=45, null=False,blank=False)
    email =models.EmailField('email',max_length=45, null=False,blank=False)
    telefono =models.CharField('telefono',max_length=45, null=False,blank=False)
    area_desempeño =models.CharField('area desempeño',max_length=45, null=False,blank=False)
    especialidad = models.CharField('especialidad',max_length=45)#nuevo
 

class Signos_vitales (models.Model):
    id_signos_vitales = models.AutoField(primary_key=True)
    fecha_registro = models.DateField('fecha_registro',auto_now=False,auto_now_add=True)
    oximetria = models.CharField('oximetria',max_length=45)
    frecuencia_respiratoria = models.CharField('frecuencia respiratoria',max_length=45)
    temperatura = models.CharField('temperatura',max_length=45)
    presion_arterial = models.CharField('presion arterial',max_length=45)
    glicemias =  models.CharField('glicemias',max_length=45)
    id_paciente = models.ForeignKey(Paciente, related_name='signos_vitales', on_delete=models.CASCADE)
    


    
