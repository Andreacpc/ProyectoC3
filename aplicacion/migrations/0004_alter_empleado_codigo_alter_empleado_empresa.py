# Generated by Django 4.1 on 2022-09-25 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_empleado_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='codigo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.empresas'),
        ),
    ]