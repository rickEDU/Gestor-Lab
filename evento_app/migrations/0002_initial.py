# Generated by Django 4.0.5 on 2022-07-08 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('laboratorio_app', '0001_initial'),
        ('evento_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='laboratorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='laboratorio_app.lab'),
        ),
    ]
