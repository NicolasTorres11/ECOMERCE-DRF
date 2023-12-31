# Generated by Django 4.2.3 on 2023-07-11 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Actualizacion')),
                ('deleted_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria del Producto',
                'verbose_name_plural': 'Categorias de los Productos',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Actualizacion')),
                ('deleted_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Medida Unitaria',
                'verbose_name_plural': 'Medidas Unitarias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Actualizacion')),
                ('deleted_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Producto')),
                ('description', models.TextField(verbose_name='Descripcion del Producto')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Actualizacion')),
                ('deleted_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
                ('discount_value', models.PositiveSmallIntegerField(default=0)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Indicador de Descuento')),
            ],
            options={
                'verbose_name': 'Inicador de Descuento',
                'verbose_name_plural': 'Indicadores de Descuento',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('updated_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Actualizacion')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Producto')),
                ('description', models.TextField(verbose_name='Descripcion del Producto')),
                ('product_image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Producto',
                'verbose_name_plural': 'historical Productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMeasureUnit',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('updated_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Actualizacion')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Medida Unitaria',
                'verbose_name_plural': 'historical Medidas Unitarias',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIndicator',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('updated_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Actualizacion')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('discount_value', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Indicador de Descuento')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Inicador de Descuento',
                'verbose_name_plural': 'historical Indicadores de Descuento',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategoryProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('updated_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Actualizacion')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('measure_unit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de Medida')),
            ],
            options={
                'verbose_name': 'historical Categoria del Producto',
                'verbose_name_plural': 'historical Categorias de los Productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
    ]
