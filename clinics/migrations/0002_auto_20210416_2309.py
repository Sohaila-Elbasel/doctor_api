# Generated by Django 3.2 on 2021-04-16 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinics', to='clinics.doctor'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_reservations', to='clinics.clinic'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_reservations', to='clinics.patient'),
        ),
    ]
