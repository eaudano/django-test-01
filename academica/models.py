from django.db import models
from django.utils import timezone
import logging

LOG = logging.getLogger(__name__)


class Alumno(models.Model):
    # legajo = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def inscripcion(self):
        LOG.debug('The new alumno is {}, {}'.format(
            self.apellido, self.nombre))
        self.save()

    def aprobo_curso_ingreso(self):
        LOG.debug('{}, {} aprobado'.format(self.apellido, self.nombre))
        pass

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)
