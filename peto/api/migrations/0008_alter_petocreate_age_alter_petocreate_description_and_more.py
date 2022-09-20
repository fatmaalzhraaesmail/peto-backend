# Generated by Django 4.1.1 on 2022-09-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_imageanimal_petocreate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petocreate',
            name='age',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='petocreate',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='petocreate',
            name='image',
            field=models.ImageField(null=True, upload_to='api/images'),
        ),
        migrations.AlterField(
            model_name='petocreate',
            name='petname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='petocreate',
            name='species',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
