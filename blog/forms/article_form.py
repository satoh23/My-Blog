from django import forms

from blog.models import article


class ArticleCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = article.Article
        fields = ('title', 'text', 'image', 'category_id')
