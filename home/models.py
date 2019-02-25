from django.db import models



class Contacto(models.Model):
    nombre = models.CharField(max_length=15)
    correo = models.EmailField(blank=True)
    mensaje = models.TextField()

    def __unicode__(self):
        return self.nombre