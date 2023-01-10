from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'thumbnail', 'category', 'created_at')
    list_display_links = ('title', 'thumbnail')
    search_fields = ('title', 'category', 'tags')
    list_filter = ('category', 'tags')
    fields = ('title', 'slug', 'text', 'category', 'tags', 'image', 'views', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    # save_as = True
    save_on_top = True
    readonly_fields = ('created_at', 'views')


    def thumbnail(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100">'.format(obj.image.url))
        return mark_safe('<img src="/media/no_image.jpg" width="100">')

    thumbnail.short_description = 'Image'