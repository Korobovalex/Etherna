from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Post, Category, Tag
from django.db.models import F
from django.urls import reverse_lazy


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


class NewsCreateView(CreateView):
    model = Post
    template_name = 'news_form.html'
    fields = '__all__'
    # fields = ['title', 'tex]
    success_url = reverse_lazy('news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add new post'
        return context


class NewsEditView(UpdateView):
    model = Post
    template_name = 'news_form.html'
    fields = '__all__'
    success_url = reverse_lazy('news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit post'
        return context


class NewsDeleteView(DeleteView):
    model = Post
    template_name = 'news_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete post'
        return context

