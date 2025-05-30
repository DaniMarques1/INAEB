# Generated by Django 5.1.6 on 2025-04-22 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_familia_data_visita_familia_obs_responsavel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='agua',
            field=models.CharField(blank=True, choices=[('Encanada', 'Encanada'), ('Poço', 'Poço'), ('Cisterna', 'Cisterna')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='banheiro',
            field=models.CharField(blank=True, choices=[('Banheiro Externo', 'Banheiro Externo'), ('Banheiro Interno', 'Banheiro Interno')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='construcao',
            field=models.CharField(blank=True, choices=[('Alvenaria', 'Alvenaria'), ('Taipa', 'Taipa'), ('Madeira', 'Madeira')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='esgoto',
            field=models.CharField(blank=True, choices=[('Rede', 'Rede'), ('Fossa', 'Fossa'), ('Céu Aberto', 'Céu Aberto')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='limpeza_casa',
            field=models.CharField(blank=True, choices=[('Varre', 'Varre'), ('Lava', 'Lava'), ('Ambos', 'Ambos')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='lixo',
            field=models.CharField(blank=True, choices=[('Queima', 'Queima'), ('Enterra', 'Enterra'), ('Coleta', 'Coleta')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='status_atendimento',
            field=models.CharField(choices=[('Ativa', 'Ativa'), ('Suspensa', 'Suspensa'), ('Aguardando Vaga', 'Aguardando Vaga')], max_length=20),
        ),
        migrations.AlterField(
            model_name='familia',
            name='tipo_moradia',
            field=models.CharField(blank=True, choices=[('Própria', 'Própria'), ('Alugada', 'Alugada'), ('Cedida', 'Cedida')], max_length=20, null=True),
        ),
    ]
