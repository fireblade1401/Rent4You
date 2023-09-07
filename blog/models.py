# Импортирование стандартной модели пользователя Django
from django.contrib.auth.models import User
# Импортирование модуля для работы с моделями базы данных
from django.db import models


# Модель блога
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='blogs')
    date = models.DateField()

    # Строковое представление объекта модели
    def __str__(self):
        return self.title

    # Метаинформация о модели
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер Новых авто'


# Модель отзывов
class FeedBacks(models.Model):
    CHOISES = (
        ('male', 'Мужчина'),
        ('female', 'Женщина'),
    )
    text = models.CharField(max_length=255)
    gender = models.CharField(choices=CHOISES, max_length=10)
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)

    # Строковое представление объекта модели
    def __str__(self):
        return self.name

    # Метаинформация о модели
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Слайды Отзывов'


# Модель для формы обратной связи
class Callback(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    # Строковое представление объекта модели
    def __str__(self):
        return self.name

    # Метаинформация о модели
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Форма обращения'


# Модель слайдера приветствия
class TitleSlider(models.Model):
    text = models.CharField(max_length=128)

    # Строковое представление объекта модели
    def __str__(self):
        return self.text

    # Метаинформация о модели
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер на Приветствии'


# Модель для кнопок обратной связи
class FeedbackButtons(models.Model):
    GeoSrc = models.URLField()
    PhoneTel = models.CharField(max_length=20)
    MailTo = models.EmailField()

    # Строковое представление объекта модели
    def __str__(self):
        return f"{self.GeoSrc}, {self.PhoneTel}, {self.MailTo}"

    # Метаинформация о модели
    class Meta:
        verbose_name = 'Добавить виды связи'
        verbose_name_plural = 'Виды связей на кнопках'


# Модель марок автомобилей
class СarMark(models.Model):
    name = models.CharField(max_length=255, unique=True)

    # Строковое представление объекта модели
    def __str__(self):
        return self.name

    # Метаинформация о модели
    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марки авто'


# Модель автомобиля
class Car(models.Model):
    mark = models.ForeignKey(СarMark, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    in_rental = models.BooleanField(default=True)

    # Строковое представление объекта модели
    def __str__(self):
        return f"{self.year} {self.mark.name} {self.model}"

    # Метаинформация о модели
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


# Модель запроса на аренду авто
class Requests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    mark = models.ForeignKey(СarMark, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=255, blank=True)
    year = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='rented_cars', blank=True)
    rented_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # При сохранении запроса на аренду, данные о марке, модели и т.д. копируются из соответствующего автомобиля
        self.make = self.car.mark
        self.model = self.car.model
        self.year = self.car.year
        self.color = self.car.color
        self.price = self.car.price
        self.image = self.car.image
        super(Requests, self).save(*args, **kwargs)

    # Строковое представление объекта модели
    def __str__(self):
        return f"{self.car}, {self.price}, {self.rented_date}"

    # Метаинформация о модели
    class Meta:
        verbose_name = 'Арендованную машину'
        verbose_name_plural = 'Арендованные машины'
