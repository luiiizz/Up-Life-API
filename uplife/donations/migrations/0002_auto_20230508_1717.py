# Generated by Django 3.2.19 on 2023-05-08 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipients', '0001_initial'),
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonation',
            name='expiry_date',
            field=models.DateField(default=None, verbose_name='data de validade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicinedonation',
            name='validation_date',
            field=models.DateTimeField(default=None, verbose_name='data de validação'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='bag_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recipients.bagtype', verbose_name='doador'),
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=50, verbose_name='tipo sanguíneo'),
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='doador'),
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='validation_date',
            field=models.DateTimeField(verbose_name='data de validação'),
        ),
        migrations.AlterField(
            model_name='medicinedonation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='doador'),
        ),
        migrations.AlterField(
            model_name='medicinedonation',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recipients.medicinetype', verbose_name='medicamento'),
        ),
    ]