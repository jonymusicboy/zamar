# Generated by Django 4.2.2 on 2023-06-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image1',
            field=models.ImageField(null=True, upload_to='staic/eventos/img', verbose_name='Imagen 1'),
        ),
        migrations.AddField(
            model_name='page',
            name='image2',
            field=models.ImageField(null=True, upload_to='staic/eventos/img/', verbose_name='Imagen 2'),
        ),
        migrations.AddField(
            model_name='page',
            name='image3',
            field=models.ImageField(null=True, upload_to='staic/eventos/img/', verbose_name='Imagen 3'),
        ),
        migrations.AddField(
            model_name='page',
            name='image4',
            field=models.ImageField(null=True, upload_to='staic/eventos/img/', verbose_name='Imagen 4'),
        ),
        migrations.AddField(
            model_name='page',
            name='image5',
            field=models.ImageField(null=True, upload_to='staic/eventos/img/', verbose_name='Imagen 5'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
    ]