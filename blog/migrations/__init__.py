from blog.forms import CarSearchForm
from blog.models import Car


def __init__(self, *args, **kwargs):
    super(CarSearchForm, self).__init__(*args, **kwargs)

    # Dynamically update choices for color
    self.fields['color'].choices = [(color, color) for color in Car.objects.values_list('color', flat=True).distinct()]

    # Dynamically update choices for year
    self.fields['year'].choices = [(year, year) for year in Car.objects.values_list('year', flat=True).distinct()]
