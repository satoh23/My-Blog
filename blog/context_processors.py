from .models import Article, Category


def common(request):
    """ テンプレートに毎回渡すデータ """
    context = {
        'category_list': Category.objects.all(),
        'thumbnail_list': Article.objects.select_related('category_id').order_by('-created_date')[:3]
    }
    return context
