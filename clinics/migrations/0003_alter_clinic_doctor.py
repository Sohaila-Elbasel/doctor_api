# Generated by Django 3.2 on 2021-04-16 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0002_auto_20210416_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clinics', to='clinics.doctor'),
        ),
    ]
