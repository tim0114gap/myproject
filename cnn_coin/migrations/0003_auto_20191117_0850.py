# Generated by Django 2.2.6 on 2019-11-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnn_coin', '0002_remove_imagemodel_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
