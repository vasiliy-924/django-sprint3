from django.contrib import admin
from .models import Category, Location, Post

admin.site.site_header = 'Панель администратора Блога'
admin.site.site_title = 'Администрирование блога'
admin.site.index_title = 'Добро пожаловать в админ-панель Блога'
admin.site.empty_value_display = 'Не задано'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title', 'description')
    list_filter = ('is_published', 'created_at')
    ordering = ('-created_at',)
    empty_value_display = 'Не задано'

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')
    ordering = ('name',)
    empty_value_display = 'Не задано'

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'pub_date', 'category', 
        'location', 'is_published', 'created_at'
    )
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'pub_date', 'category', 'location')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    raw_id_fields = ('author',)
    empty_value_display = 'Не задано'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)