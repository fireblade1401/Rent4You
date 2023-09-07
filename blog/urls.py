#  Импортируем path для определения маршрутов URL и views, где находятся функции представлений.
from django.urls import path
from . import views

# Определяем маршруты URL для вашего приложения.
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('cars/', views.cars, name="cars"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name="profile"),
]