# Generated by Django 3.0.7 on 2020-06-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_account', '0002_auto_20200622_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]