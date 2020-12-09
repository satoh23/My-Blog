from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'blog'

urlpatterns = [
    path('', cache_page(60 * 15)(views.BlogHome.as_view()), name='home'),
    path('category/<int:pk>/', views.BlogCategory.as_view(), name='category'),
    path('detail/<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    path('comment/<int:article_pk>/', views.BlogComment.as_view(), name='comment'),
    path('article-create/', views.Article_create.as_view(), name='article_create'),
]
