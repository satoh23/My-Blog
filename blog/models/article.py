from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from .category import Category


class Article(models.Model):
    """ ブログの記事 """

    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('本文')
    thumbnail = ProcessedImageField(upload_to='thumbnails/', processors=[ResizeToFill(500, 333)],
                                    format='JPEG', options={'quality': 60}, null=True, blank=True)
    created_date = models.DateTimeField('作成日', auto_now_add=True)
    category_id = models.ForeignKey(
        Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
