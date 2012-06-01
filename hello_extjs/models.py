from django.db import models

class Usuarios(models.Model):
	nome = models.CharField(max_length=256, blank=True)
	email = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.nome