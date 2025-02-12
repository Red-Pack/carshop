# Generated by Django 5.1.1 on 2025-02-09 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Марка')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('vin', models.CharField(max_length=17, unique=True, verbose_name='VIN')),
                ('is_new', models.BooleanField(default=False, verbose_name='Новая машина')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('owners', models.PositiveIntegerField(verbose_name='Количество владельцев')),
                ('mileage', models.PositiveIntegerField(verbose_name='Пробег')),
                ('body_type', models.CharField(choices=[('седан', 'Седан'), ('хэтчбек', 'Хэтчбек'), ('универсал', 'Универсал'), ('внедорожник', 'Внедорожник'), ('купе', 'Купе')], max_length=20, verbose_name='Тип кузова')),
                ('transmission', models.CharField(choices=[('MT', 'механика'), ('AT', 'автомат'), ('CVT', 'вариатор'), ('DCT', 'робот')], max_length=20, verbose_name='КПП')),
                ('drive', models.CharField(choices=[('передний', 'Передний'), ('задний', 'Задний'), ('полный', 'Полный')], max_length=20, verbose_name='Привод')),
                ('wheel', models.CharField(choices=[('левый', 'Левый'), ('правый', 'Правый')], max_length=10, verbose_name='Руль')),
                ('color', models.CharField(max_length=20, verbose_name='Цвет')),
                ('engine', models.CharField(choices=[('бензин', 'Бензин'), ('дизель', 'Дизель'), ('электричество', 'Электричество'), ('гибрид', 'Гибрид')], max_length=20, verbose_name='Двигатель')),
                ('engine_capacity', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Объем двигателя (л)')),
                ('power_hp', models.PositiveIntegerField(verbose_name='Мощность (л.с.)')),
                ('doors', models.PositiveIntegerField(verbose_name='Количество дверей')),
                ('generation', models.CharField(max_length=50, verbose_name='Поколение')),
                ('modification', models.CharField(max_length=50, verbose_name='Модификация')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Фото')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cars.car')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Модель')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='cars.brand', verbose_name='Марка')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel', verbose_name='Модель'),
        ),
    ]
