# Generated by Django 4.1.1 on 2022-09-16 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_petocreate_petname'),
    ]

    operations = [
        migrations.AddField(
            model_name='petocreate',
            name='image',
            field=models.ImageField(null=True, upload_to='peto/images'),
        ),
    ]