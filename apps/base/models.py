from django.db import models
import random
from apps.users.models import User


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de Creacion', auto_now_add=True, auto_now=False)
    updated_date = models.DateField('Fecha de Actualizacion', auto_now_add=True, auto_now=False)
    deleted_date = models.DateField('Fecha de Eliminacion', auto_now_add=True, auto_now=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Bases'


class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)  # Código de 6 dígitos
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Code: {self.code} - User: {self.user}"
