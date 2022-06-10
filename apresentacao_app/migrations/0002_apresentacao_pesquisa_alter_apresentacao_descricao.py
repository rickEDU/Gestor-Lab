# Generated by Django 4.0.5 on 2022-06-10 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linhapesquisa_app', '0002_linhapesquisa_laboratorio_pesq'),
        ('apresentacao_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apresentacao',
            name='pesquisa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='linhapesquisa_app.linhapesquisa'),
        ),
        migrations.AlterField(
            model_name='apresentacao',
            name='descricao',
            field=models.TextField(),
        ),
    ]
