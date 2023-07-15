from django.contrib import admin
from mptt.admin import MPTTModelAdmin#дерево в админке категорий

from . import models


class RecipeInline(admin.StackedInline):
    model = models.Recipe#к посту прикрепить рецепт в админке
    extra = 1#один рецепт



class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'create_at', 'id']
    inlines = [RecipeInline]#к посту прикрепить рецепт в админке
    save_as = True
    save_on_top = True#кнопка сохранить вверху админки


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
#admin.site.register(models.Recipe)
admin.site.register(models.Comment)