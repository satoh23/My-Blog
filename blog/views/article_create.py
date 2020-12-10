from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views import generic

from blog.forms import article_form
from blog.models import article


class Article_create(UserPassesTestMixin, generic.CreateView):
    """ 記事作成(スーパーユーザーのみ可) """
    model = article.Article
    form_class = article_form.ArticleCreateForm
    template_name = 'blog/article_create_form.html'

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        article_data = form.save(commit=False)
        article_data.save()
        return redirect('blog:home')
