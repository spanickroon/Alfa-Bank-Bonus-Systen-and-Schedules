# Generated by Django 3.0.7 on 2020-06-29 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alfastaff_bonuses', '0011_auto_20200626_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonuscard',
            name='cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='image',
            field=models.ImageField(blank=True, default='bonuses/product.jpg', null=True, upload_to='bonuses', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='balance',
            field=models.IntegerField(blank=True, null=True, verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоимость товара'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date_buy',
            field=models.DateField(auto_now=True, null=True, verbose_name='Дата покупки'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='id_purchase',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Одобрено'), (2, 'Отменено'), (3, 'Ожидание')], null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользоваетль'),
        ),
    ]
