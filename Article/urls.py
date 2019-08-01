from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    path('',cache_page(60 * 15)(views.home),name='home'),
    path('articles/',cache_page(60 * 15)(views.Articles_list), name='articles_list'),
    path('article/<str:article_slug>', cache_page(60 * 15)(views.detail), name='detail'),
    path('categories/<str:category_slug>/', views.list_of_articles_by_category, name='category_list'),

    path('tags/<str:tags_slug>/', (views.tagged), name='tagged'),
    path('search',views.search, name='search'),


    path('events/', cache_page(60 * 15)(views.events), name='events'),

]
