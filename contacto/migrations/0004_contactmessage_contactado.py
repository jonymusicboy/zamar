# Generated by Django 4.2.2 on 2023-06-26 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0003_contactmessage_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='contactado',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
