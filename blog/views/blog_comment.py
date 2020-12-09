from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from blog.forms import comment_form
from blog.models import article, comment


class BlogComment(generic.CreateView):
    """ ブログのコメント """
    model = comment.Comment
    form_class = comment_form.CommentCreateForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        article_pk = self.kwargs['article_pk']
        comment = form.save(commit=False)
        comment.article_id = get_object_or_404(article.Article, pk=article_pk)
        comment.save()
        return redirect('blog:detail', pk=article_pk)
