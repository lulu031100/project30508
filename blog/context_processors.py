# このファイルはカテゴリ一覧をテンプレートで使用するためにcontextを自前で用意するために作った
from .models import Category
from django.db.models import Count, Q

def common(request):
    context = {
        'category_list':Category.objects.all(),
    }
    return context