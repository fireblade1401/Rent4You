# Импортируем модуль форм Django
from django import forms
# Импортируем модели из текущего приложения
from .models import Callback, СarMark, Car


# Определяем форму обратного вызова, которая будет связана с моделью Callback.
class CallbackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = ['name', 'phone', 'email', 'message']


# Определяем форму для поиска автомобилей
class CarSearchForm(forms.Form):
    make = forms.ModelChoiceField(queryset=СarMark.objects.all(), required=False, widget=forms.Select,
                                  empty_label="Выберите марку")
    model = forms.CharField(required=False)
    color = forms.ChoiceField(choices=[], required=False)
    year = forms.ChoiceField(choices=[], required=False)

    # Переопределенный метод инициализации для формы
    def __init__(self, *args, **kwargs):
        super(CarSearchForm, self).__init__(*args, **kwargs)
        # Устанавливаем доступные значения для выбора цвета из имеющихся в базе данных автомобилей
        self.fields['color'].choices = [("", "Все")] + list(set([(car.color, car.color) for car in Car.objects.all()]))
        # Устанавливаем доступные значения для выбора года выпуска из имеющихся в базе данных автомобилей
        self.fields['year'].choices = [("", "Все")] + list(set([(car.year, car.year) for car in Car.objects.all()]))
