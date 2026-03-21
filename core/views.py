from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        messages.success(request, f'Спасибо, {name}! Ваша заявка принята, мы свяжемся с вами.')
        return redirect('home')
    return render(request, 'reservation.html')

def contacts(request):
    return render(request, 'contacts.html')