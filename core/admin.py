from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Dish, NewsArticle


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # slug заполняется автоматически


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'name', 'category', 'price', 'is_available', 'is_hit')
    list_display_links = ('name',)
    list_editable = ('is_available', 'is_hit')   # редактировать прямо в списке
    list_filter = ('category', 'is_available', 'is_hit')
    search_fields = ('name', 'description')

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px; height:45px; object-fit:cover; border-radius:4px;">',
                obj.image.url
            )
        return '—'
    preview_image.short_description = 'Фото'


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'title', 'category', 'is_featured', 'is_published', 'created_at')
    list_display_links = ('title',)
    list_editable = ('is_featured', 'is_published')
    list_filter = ('category', 'is_published', 'is_featured')
    search_fields = ('title', 'excerpt', 'content')

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px; height:45px; object-fit:cover; border-radius:4px;">',
                obj.image.url
            )
        return '—'
    preview_image.short_description = 'Фото'