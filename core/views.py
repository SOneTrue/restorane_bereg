from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def news(request):
    category = request.GET.get('category')
    # Временные данные — потом заменим на модели из БД
    return render(request, 'news.html', {
        'news_list': [],
        'featured_news': None,
        'current_category': category,
    })

def news_detail(request, pk):
    # article = get_object_or_404(NewsArticle, pk=pk)  # раскомментировать после моделей
    return render(request, 'news_detail.html', {
        # 'article': article
    })

def menu(request):
    return render(request, 'menu.html')

def dish_detail(request, pk):
    # dish = get_object_or_404(Dish, pk=pk)
    # related_dishes = Dish.objects.filter(category=dish.category).exclude(pk=pk)[:3]
    return render(request, 'dish_detail.html', {
        # 'dish': dish,
        # 'related_dishes': related_dishes,
    })

def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        messages.success(request, f'Спасибо, {name}! Ваша заявка принята.')
        return redirect('home')
    return render(request, 'reservation.html')

def contacts(request):
    return render(request, 'contacts.html')