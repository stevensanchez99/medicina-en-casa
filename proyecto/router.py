from aplicacion.viewsets import FamiliarViewset, Historia_clinicaViewset, PacienteViewset, Personal_medicoViewset, Signos_vitalesViewset
from rest_framework import routers

#se importan las vistas de viewsets
#el nombre entre comillas indica como vamos a acceder por medio de la url en el navegador y se llama la vista a la cual hace referencia.

router = routers.DefaultRouter()
router.register('pacientes', PacienteViewset)
router.register('familiar', FamiliarViewset)
router.register('historia', Historia_clinicaViewset)
router.register('medico', Personal_medicoViewset)
router.register('signos', Signos_vitalesViewset)



