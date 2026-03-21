from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Dish, Category, NewsArticle, Reservation  # ← добавлен Reservation


def home(request):
    news_preview = NewsArticle.objects.filter(is_published=True)[:3]
    return render(request, 'home.html', {'news_preview': news_preview})


def news(request):
    category = request.GET.get('category')
    articles = NewsArticle.objects.filter(is_published=True)
    if category:
        articles = articles.filter(category=category)
    featured = NewsArticle.objects.filter(is_published=True, is_featured=True).first()
    return render(request, 'news.html', {
        'news_list': articles,
        'featured_news': featured,
        'current_category': category,
    })


def news_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk, is_published=True)
    return render(request, 'news_detail.html', {'article': article})


def menu(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()
    dishes = Dish.objects.filter(is_available=True).select_related('category')
    if category_slug:
        dishes = dishes.filter(category__slug=category_slug)
    return render(request, 'menu.html', {
        'dishes': dishes,
        'categories': categories,
        'current_category': category_slug,
    })


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk, is_available=True)
    related_dishes = Dish.objects.filter(
        category=dish.category, is_available=True
    ).exclude(pk=pk)[:3]
    return render(request, 'dish_detail.html', {
        'dish': dish,
        'related_dishes': related_dishes,
    })


def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests', '2')
        comment = request.POST.get('comment', '').strip()

        # ← сохраняем заявку в БД
        Reservation.objects.create(
            name=name,
            phone=phone,
            date=date,
            time=time,
            guests=guests,
            comment=comment,
        )

        messages.success(request, f'Спасибо, {name}! Ваша заявка принята — мы свяжемся с вами.')
        return redirect('home')

    return render(request, 'reservation.html')


def contacts(request):
    return render(request, 'contacts.html')