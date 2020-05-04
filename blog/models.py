from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

app_name = 'blog'

class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=200)
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.name
class Post(models.Model):

    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('本文')
    # MEDIA_ROOTからの相対パスを指定　ここに保存される
    image = models.ImageField(upload_to='',blank=True, null=True)
    created_at = models.DateTimeField('作成日',default=timezone.now)
    created_user = models.ForeignKey(User, verbose_name = '登録ユーザー', blank=True, null=True, on_delete = models.PROTECT
    )
    category = models.ForeignKey(
        Category, verbose_name = 'カテゴリ', on_delete = models.PROTECT
    )
 
    def __str__(self):
        return self.title


