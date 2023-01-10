from django import template
from news.models import Category
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('tags/cats-widget_tpl.html')
def show_cats():
    categories = Category.objects.all().annotate(posts_count=Count('posts'))
    return {'categories': categories}
