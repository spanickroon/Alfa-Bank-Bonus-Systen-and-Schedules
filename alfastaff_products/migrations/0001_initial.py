# Generated by Django 3.0.7 on 2020-09-30 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='Стоимость')),
                ('image', models.ImageField(blank=True, default='products/product.jpg', null=True, upload_to='products', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'Продукты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название продукта')),
                ('id_purchase', models.IntegerField(blank=True, null=True, verbose_name='ID')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='Стоимость продукта')),
                ('date_buy', models.DateField(auto_now=True, null=True, verbose_name='Дата покупки')),
                ('balance', models.IntegerField(blank=True, null=True, verbose_name='Остаток')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Одобрено'), (2, 'Отменено'), (3, 'Ожидание')], null=True, verbose_name='Статус')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользоваетль')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
                'ordering': ['-id'],
            },
        ),
    ]
