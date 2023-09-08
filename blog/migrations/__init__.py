from blog.forms import CarSearchForm
from blog.models import Car


def __init__(self, *args, **kwargs):
    super(CarSearchForm, self).__init__(*args, **kwargs)

    # Динамическое обновление по цвету
    self.fields['color'].choices = [(color, color) for color in Car.objects.values_list('color', flat=True).distinct()]

    # Динамическое обновление по годам
    self.fields['year'].choices = [(year, year) for year in Car.objects.values_list('year', flat=True).distinct()]
