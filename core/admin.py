from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Dish, NewsArticle, Reservation
from .models import NewsSubscriber

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


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'guests', 'status_badge', 'status', 'created_at')
    list_display_links = ('name',)           # ← обязательно, иначе конфликт с list_editable
    list_editable = ('status',)
    list_filter = ('status', 'date')
    search_fields = ('name', 'phone')
    readonly_fields = ('created_at',)
    date_hierarchy = 'date'

    def status_badge(self, obj):
        colors = {
            'new': '#ff0055',
            'confirmed': '#22c55e',
            'cancelled': '#6b7280',
        }
        color = colors.get(obj.status, '#fff')
        return format_html(
            '<span style="background:{}; color:white; padding:3px 10px; border-radius:4px; font-size:12px; font-weight:bold;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Статус'


@admin.register(NewsSubscriber)
class NewsSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('email',)

