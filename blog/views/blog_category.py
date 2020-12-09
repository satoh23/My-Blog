from django.shortcuts import get_object_or_404
from django.views import generic

from blog.models import article, category


class BlogCategory(generic.ListView):
    """ 選択したカテゴリで絞り込む """
    model = article.Article
    paginate_by = 10
    template_name = 'blog/blog_home.html'

    def get_queryset(self):
        category_id = get_object_or_404(
            category.Category, pk=self.kwargs['pk'])
        queryset = article.Article.objects.select_related('category_id').order_by(
            '-created_date').filter(category_id=category_id)
        return queryset
