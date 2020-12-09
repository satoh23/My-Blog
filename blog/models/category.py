from django.db import models


class Category(models.Model):
    """ ブログのカテゴリー """
    name = models.CharField('カテゴリ名', max_length=255)
    created_date = models.DateTimeField('作成日', auto_now_add=True)

    def __str__(self):
        return self.name
