from django.db.models import Q
from django.views import generic

from blog.models import article


class BlogHome(generic.ListView):
    """ ブログのホーム画面 """
    model = article.Article
    paginate_by = 10
    template_name = 'blog/blog_home.html'

    # ブログを新しい順で表示する
    def get_queryset(self):
        queryset = article.Article.objects.select_related('category_id').order_by('-created_date')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset
