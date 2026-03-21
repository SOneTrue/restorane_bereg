# core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
# from menu.models import Dish, Category  # Раскомментировать позже
# from .models import Event

def home(request):
    # events = Event.objects.all()[:3]
    return render(request, 'home.html', {
        # 'events': events
    })

def menu(request):
    # categories = Category.objects.all()
    # dishes = Dish.objects.filter(is_available=True)
    return render(request, 'menu.html', {
        # 'categories': categories,
        # 'dishes': dishes,
    })

def reservation(request):
    if request.method == 'POST':
        # Обработка формы (добавим позже)
        messages.success(request, 'Ваша заявка принята! Менеджер свяжется с вами.')
        return redirect('home')
    return render(request, 'reservation.html')

def contacts(request):
    return render(request, 'contacts.html')