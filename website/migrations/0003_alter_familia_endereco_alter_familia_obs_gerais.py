# Generated by Django 5.1.6 on 2025-04-14 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_doacao_options_alter_itemcesta_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='endereco',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familia',
            name='obs_gerais',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
