from django.db import models

from .article import Article


class Comment(models.Model):
    """ ブログのコメント """

    name = models.CharField('名前', max_length=30, default='名無し')
    text = models.TextField('本文')
    article_id = models.ForeignKey(Article, verbose_name='紐付く記事', on_delete=models.PROTECT)
    created_date = models.DateTimeField('作成日', auto_now_add=True)

    def __str__(self):
        return self.text[:10]
