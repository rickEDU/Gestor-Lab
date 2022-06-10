# Generated by Django 4.0.5 on 2022-06-10 17:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('membros_app', '0003_alter_membro_laboratorio_alter_membro_membro_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
