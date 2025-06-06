# Generated by Django 5.1.6 on 2025-04-22 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_familia_status_atendimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familia',
            old_name='obs_esgoto',
            new_name='obs_saneamento',
        ),
        migrations.AlterField(
            model_name='familia',
            name='bairro',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familia',
            name='cep',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='familia',
            name='cidade',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='familia',
            name='despesa_apro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='receita_apro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
