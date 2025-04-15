# Generated by Django 5.1.6 on 2025-04-15 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_familia_endereco_alter_familia_obs_gerais'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='data_visita',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='familia',
            name='obs_responsavel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='data_entrevista',
            field=models.DateField(blank=True, null=True),
        ),
    ]
