from django.contrib import admin
from .models import Post
from .models import Group

class PostAdmin(admin.ModelAdmin):
    list_editable = ('group',)
    list_display = ('pk', 'text', 'pub_date', 'author', 'group') # Перечисляем поля, которые должны отображаться в админке
    search_fields = ('text',) # Добавляем интерфейс для поиска по тексту постов
    list_filter = ('pub_date',) # Добавляем возможность фильтрации по дате
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-'
# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group)

# Register your models here.
