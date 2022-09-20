# Generated by Django 4.1.1 on 2022-09-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=150)),
                ('image', models.ImageField(null=True, upload_to='./account/images')),
            ],
        ),
    ]
