# Generated by Django 3.0.7 on 2020-07-21 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_bonuses', '0018_bonuscard_image_ыек'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bonuscard',
            old_name='image_ыек',
            new_name='image_str',
        ),
    ]