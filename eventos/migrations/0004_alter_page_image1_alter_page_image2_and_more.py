# Generated by Django 4.2.2 on 2023-06-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_alter_page_image1_alter_page_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image1',
            field=models.ImageField(null=True, upload_to='../../eventos/static/eventos/img', verbose_name='Imagen 1'),
        ),
        migrations.AlterField(
            model_name='page',
            name='image2',
            field=models.ImageField(null=True, upload_to='../../eventos/static/eventos/img', verbose_name='Imagen 2'),
        ),
        migrations.AlterField(
            model_name='page',
            name='image3',
            field=models.ImageField(null=True, upload_to='../../eventos/static/eventos/img', verbose_name='Imagen 3'),
        ),
        migrations.AlterField(
            model_name='page',
            name='image4',
            field=models.ImageField(null=True, upload_to='../../eventos/static/eventos/img', verbose_name='Imagen 4'),
        ),
        migrations.AlterField(
            model_name='page',
            name='image5',
            field=models.ImageField(null=True, upload_to='../../eventos/static/eventos/img', verbose_name='Imagen 5'),
        ),
    ]
