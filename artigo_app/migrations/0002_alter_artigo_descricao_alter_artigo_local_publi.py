# Generated by Django 4.0.5 on 2022-06-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='local_Publi',
            field=models.URLField(),
        ),
    ]
