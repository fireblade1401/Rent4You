# Импортируем стандартный модуль администрирования Django
from django.contrib import admin
# Импортируем модели из текущего приложения
from .models import Blog, FeedBacks, Callback, TitleSlider, FeedbackButtons, СarMark, Car, Requests

# Регистрируем модели, для отображения в админ-панели Django
admin.site.register(Blog)
admin.site.register(FeedBacks)
admin.site.register(Callback)
admin.site.register(TitleSlider)
admin.site.register(FeedbackButtons)
admin.site.register(СarMark)
admin.site.register(Car)
admin.site.register(Requests)