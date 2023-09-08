# Импорт декоратора, который требует, чтобы пользователь был аутентифицирован перед доступом к определенной view.
from django.contrib.auth.decorators import login_required

# Импорт метода, для отправки сообщения пользователю
from django.contrib import messages

# Импорт метода для рендеринга шаблонов.
from django.shortcuts import render

# Импорт класса для постраничного вывода объектов
from django.core.paginator import Paginator

# Импорт методов для аутентификации пользователей, входа и выхода.
from django.contrib.auth import authenticate, login, logout

# Импорт утилит для редиректа и поиска объектов с возможностью выброса исключения,
# если объект не найден.
from django.shortcuts import redirect, get_object_or_404

# Импорт форм для аутентификации и создания пользователей.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Импорт моделей, которые будут использоваться в этом файле views.
from .models import Blog, FeedBacks, TitleSlider, FeedbackButtons, Car, Requests

# Импорт кастомных форм, созданных для использования в этом файле views.
from .forms import CallbackForm, CarSearchForm


# Отображение главной страницы
def index(request):
    blogs = Blog.objects.all()
    feedbacks = FeedBacks.objects.all()
    title_slides = TitleSlider.objects.all()
    feedback_buttons = FeedbackButtons.objects.get(id=1)

    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CallbackForm()

    context = {
        'blogs': blogs,
        'feedbacks': feedbacks,
        'form': form,
        'titleSlides': title_slides,
        'buttons': feedback_buttons,
    }

    # Отправка данных в шаблон и отображение страницы
    return render(request, 'blog/index.html', context)


# Отображение страницы "О нас"
def about(request):
    # Просто отображает шаблон страницы "О нас"
    return render(request, 'blog/about.html')


# Отображение страницы со списком автомобилей
def cars(request):
    # Обработка поиска автомобилей и формы для аренды автомобиля
    form = CarSearchForm(request.GET)
    cars_list = Car.objects.all()

    if request.method == "POST" and 'rent_car_id' in request.POST:
        car_id = request.POST.get('rent_car_id')
        car_to_rent = get_object_or_404(Car, id=car_id)

        rented_car = Requests(car=car_to_rent, user=request.user)
        rented_car.save()

        car_to_rent.in_rental = False
        car_to_rent.save()

        messages.success(
            request,
    'Машина была успешно арендована, поздравляем! (Наши менеджера свяжутся с вами в ближайшее время)'
        )

        return redirect('cars')

    if form.is_valid():
        make = form.cleaned_data['make']
        model = form.cleaned_data['model']
        color = form.cleaned_data['color']
        year = form.cleaned_data['year']

        if make:
            cars_list = cars_list.filter(make=make)
        if model:
            cars_list = cars_list.filter(model__icontains=model)
        if color:
            cars_list = cars_list.filter(color=color)
        if year:
            cars_list = cars_list.filter(year=year)

    paginator = Paginator(cars_list, 6)
    page = request.GET.get('page')
    cars_list = paginator.get_page(page)

    context = {
        'form': form,
        'cars_list': cars_list,
    }

    # Отправка данных в шаблон и отображение страницы
    return render(request, 'blog/car.html', context)


# Отображение страницы блога
def blog(request):
    # Получаем все объекты блога для отображения
    blogs = Blog.objects.all()

    # Отправка данных в шаблон и отображение страницы
    return render(request, 'blog/blog.html', {'blogs': blogs})


# Отображение страницы для обратной связи
def contact(request):
    feedback_buttons = FeedbackButtons.objects.get(id=1)

    # Обработка формы обратного звонка
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CallbackForm()

    context = {
        'form': form,
        'buttons': feedback_buttons,
    }

    # Отправка формы в шаблон и отображение страницы входа
    return render(request, 'blog/contact.html', context)


# Контроллер входа на сайт
def login_view(request):
    # Обработка данных формы входа
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()

    # Отправка формы в шаблон и отображение страницы входа
    return render(request, 'blog/login.html', {'form': form})


def register_view(request):
    # Обработка данных формы регистрации
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    # Отправка формы в шаблон и отображение страницы регистрации
    return render(request, 'blog/register.html', {'form': form})


def logout_view(request):
    # Процесс выхода пользователя из системы
    logout(request)
    return redirect('/')


# Функция отображения профиля пользователя (только для авторизованных пользователей)
@login_required  # Декоратор, который требует, чтобы пользователь был авторизован
def profile(request):
    # Получаем все арендованные автомобили пользователя
    user = request.user
    rentals = Requests.objects.filter(user=user)

    context = {
        'rentals': rentals,
    }

    # Отправка данных в шаблон и отображение страницы профиля
    return render(request, 'blog/profile.html', context)
