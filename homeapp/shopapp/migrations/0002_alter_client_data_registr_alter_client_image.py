# Generated by Django 5.0.6 on 2024-05-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='data_registr',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(default=None, upload_to='photo/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]