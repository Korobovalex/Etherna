from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('post/<str:slug>/', views.NewsDetailView.as_view(), name='post'),
]