from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

app_name = 'blog'

class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=200)
    created_at = models.DateTimeField('作成日',default=timezone.now)
    class Meta:
        ordering = ['name']

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
    like_num = models.IntegerField(default=0) #いいねの数の追加
 
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name = 'comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = [ '-timestamp']

    def approve(self):
        self.approved = True
        self.save()
    
    def __str__(self):
        return self.text
class Reply(models.Model):
    comment = models.ForeignKey(
            Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日',default=timezone.now)
   



