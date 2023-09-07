# Generated by Django 4.2.5 on 2023-09-07 14:42

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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='blogs')),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайдер Новых авто',
            },
        ),
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Форма обращения',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='cars')),
                ('in_rental', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='FeedbackButtons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GeoSrc', models.URLField()),
                ('PhoneTel', models.CharField(max_length=20)),
                ('MailTo', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Добавить виды связи',
                'verbose_name_plural': 'Виды связей на кнопках',
            },
        ),
        migrations.CreateModel(
            name='FeedBacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Мужчина'), ('female', 'Женщина')], max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Слайды Отзывов',
            },
        ),
        migrations.CreateModel(
            name='TitleSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайдер на Приветствии',
            },
        ),
        migrations.CreateModel(
            name='СarMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Марка авто',
                'verbose_name_plural': 'Марки    авто',
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=255)),
                ('year', models.PositiveIntegerField(null=True)),
                ('color', models.CharField(blank=True, max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, upload_to='rented_cars')),
                ('rented_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.car')),
                ('mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.сarmark')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Арендованную машину',
                'verbose_name_plural': 'Арендованные машины',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.сarmark'),
        ),
    ]
