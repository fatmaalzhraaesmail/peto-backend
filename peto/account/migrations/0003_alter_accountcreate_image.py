# Generated by Django 4.1.1 on 2022-09-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_accountcreate_contact_alter_accountcreate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountcreate',
            name='image',
            field=models.ImageField(null=True, upload_to='account/images'),
        ),
    ]
