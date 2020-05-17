from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/',views.AddView.as_view(), name='add'), # http://127.0.0.1:8000/add/
    path('update/<int:pk>/',views.UpdateView.as_view(), name='update'),# http://127.0.0.1:8000/update/
    path('delete/<int:pk>/',views.DeleteView.as_view(), name='delete'),# http://127.0.0.1:8000/delete/
    path('comment/<int:pk>/', views.CommentFormView.as_view(), name='comment_form'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('reply/<int:pk>/', views.ReplyFormView.as_view(), name='reply_form'),
    path('reply/<int:pk>/approve/', views.reply_approve, name='reply_approve'),
    path('reply/<int:pk>/remove/', views.reply_remove, name='reply_remove'),
    path('like/<int:post_id>/<int:user_id>/',views.like, name='like'),
]
