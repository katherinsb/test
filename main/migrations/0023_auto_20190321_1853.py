# Generated by Django 2.0.4 on 2019-03-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20190321_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='subtitulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='titulo',
            field=models.CharField(max_length=150),
        ),
    ]
