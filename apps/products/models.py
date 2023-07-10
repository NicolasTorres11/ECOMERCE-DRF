from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords


class MeasureUnit(BaseModel):
    description = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    # MANEJO DEL HISTORIAL DE USUARIOS QUE HAN HECHO CAMBIOS EN LOS APLICATIVOS Y EN LOS MODELOS
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Medida Unitaria'
        verbose_name_plural = 'Medidas Unitarias'

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):
    description = models.CharField('Descripcion', max_length=50, unique=True, blank=False, null=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida')
    historical = HistoricalRecords()

    # TODOS LOS MODELOS QUE TENGAN LA PROPIEDAD HISTORICALRECORDS DEBEN TENER EL CODIGO DE LAS LINES 33 A LA 39
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'{self.description}'


