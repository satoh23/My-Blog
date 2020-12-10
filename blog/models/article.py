from django.db import models

from stdimage import StdImageField

from .category import Category


class Article(models.Model):
    """ ブログの記事 """

    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('本文')
    image = StdImageField(upload_to='thumbnails/', null=True, blank=True, variations={'thumbnail': (500, 333)})
    created_date = models.DateTimeField('作成日', auto_now_add=True)
    category_id = models.ForeignKey(
        Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
