# Generated by Django 3.0.7 on 2020-07-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_account', '0017_profile_avatar_binary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_binary',
            field=models.BinaryField(blank=True, editable=True, verbose_name='Фотография байткод'),
        ),
    ]