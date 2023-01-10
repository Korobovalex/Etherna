from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    # Single post operations
    path('add/', views.NewsCreateView.as_view(), name='add'),
    path('post/<str:slug>/', views.NewsDetailView.as_view(), name='post'),
    path('post/<str:slug>/edit/', views.NewsEditView.as_view(), name='edit'),
    path('post/<str:slug>/delete/', views.NewsDeleteView.as_view(), name='delete'),
    # News filters
    path('category/<str:slug>/', views.CategoryNewsList.as_view(), name='category'),
]