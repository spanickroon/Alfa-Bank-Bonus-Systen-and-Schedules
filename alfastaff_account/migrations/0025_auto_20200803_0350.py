# Generated by Django 3.0.7 on 2020-08-03 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_account', '0024_auto_20200803_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profiles/anon_user.png', null=True, upload_to='profiles', verbose_name='Аватарка профиля'),
        ),
    ]