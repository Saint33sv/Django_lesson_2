# Generated by Django 4.2 on 2023-05-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Фото'),
        ),
    ]
