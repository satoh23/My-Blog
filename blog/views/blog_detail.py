from django.views import generic

from blog.models import article


class BlogDetail(generic.DetailView):
    """ 詳細画面 """
    model = article.Article
    template_name = 'blog/article_detail.html'
