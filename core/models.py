from django.db import models


class Category(models.Model):
    """Категория блюда: Закуски, Горячее, Напитки и т.д."""
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Dish(models.Model):
    """Блюдо в меню ресторана"""
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name='Категория', related_name='dishes'
    )
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    ingredients = models.TextField('Состав', blank=True)
    price = models.DecimalField('Цена (₽)', max_digits=8, decimal_places=2)
    weight = models.PositiveIntegerField('Вес (г)', null=True, blank=True)
    calories = models.PositiveIntegerField('Калории', null=True, blank=True)
    image = models.ImageField('Фото', upload_to='dishes/', blank=True, null=True)
    is_available = models.BooleanField('В наличии', default=True)
    is_hit = models.BooleanField('Хит продаж', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    """Новость или событие ресторана"""
    CATEGORY_CHOICES = [
        ('events', 'Событие'),
        ('menu', 'Кухня'),
        ('promo', 'Акция'),
        ('bar', 'Бар'),
    ]

    title = models.CharField('Заголовок', max_length=200)
    excerpt = models.TextField('Краткое описание')
    content = models.TextField('Полный текст')
    category = models.CharField(
        'Категория', max_length=20,
        choices=CATEGORY_CHOICES, default='events'
    )
    image = models.ImageField('Фото', upload_to='news/', blank=True, null=True)
    is_featured = models.BooleanField('Главная новость', default=False)
    is_published = models.BooleanField('Опубликована', default=True)
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def __str__(self):
        return self.title