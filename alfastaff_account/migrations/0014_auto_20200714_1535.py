# Generated by Django 3.0.7 on 2020-07-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_account', '0013_auto_20200708_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='https://www.dropbox.com/home/media/profiles', verbose_name='Фотография'),
        ),
    ]
