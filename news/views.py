from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Category, Tag
from django.db.models import F


# Create your views here.
def news(request):
    return render(request, 'list.html')


class NewsListView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News list'

        return context


class NewsDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post'
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context
