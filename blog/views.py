from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin  # 追加
from django.contrib.auth.decorators import login_required

from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm, CommentForm, ReplyForm
from .models import Post, Category,Comment, Reply, Like


class IndexView(generic.ListView):
    # 初期画面で表示される全部一覧用と検索ボックスに入力した時用
    template_name = 'blog/post_list.html'
    model = Post
    paginate_by = 3 # 追加

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset

class CategoryView(generic.ListView):
    # カテゴリを選択したときに表示される一覧用
    template_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):

        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        # queryset = Post.objects.order_by('created_at').filter(category=category)
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        return queryset

class DetailView(generic.DetailView):
    # 詳細画面用
    template_name = 'blog/post_detail.html'
    model = Post
    # like


 
class AddView(LoginRequiredMixin, generic.CreateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:index')
    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['created_user'] = self.request.user
    #     return initial

    def form_valid(self, form):
        blogpost = form.save(commit=False)
        blogpost.created_user = self.request.user
        blogpost.save()
        return super().form_valid(form)

      
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:index')


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    # 削除時の確認用
    template_name = 'blog/post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('blog:index')

class CommentFormView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        post_pk = self.kwargs['pk']
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('blog:detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_pk = self.kwargs['pk']
        context['post'] = get_object_or_404(Post, pk=post_pk)
        return context

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:detail', pk=comment.post.pk)
 
 
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:detail', pk=comment.post.pk)


class ReplyFormView(LoginRequiredMixin, generic.CreateView):
    model = Reply
    form_class = ReplyForm

    def form_valid(self, form):
        reply = form.save(commit=False)
        comment_pk = self.kwargs['pk']
        reply.comment = get_object_or_404(Comment, pk=comment_pk)
        reply.save()
        return redirect('blog:detail', pk=reply.comment.post.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_pk = self.kwargs['pk']
        context['comment'] = get_object_or_404(Comment, pk=comment_pk)
        return context


@login_required
def reply_approve(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    reply.approve()
    return redirect('blog:detail', pk=reply.comment.post.pk)


@login_required
def reply_remove(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    reply.delete()
    return redirect('blog:detail', pk=reply.comment.post.pk)
@login_required
def like(request, user_id, post_id):
    """いいねボタンをクリック"""
    if request.method == 'POST':
    query = Like.objects.filter(user_id=user_id, post_id=post_id)
    if  query.count() == 0:
            like = Like()
            like.user_id = user_id
            like.post_id = post_id
            like.save()
    else
            query.delete()
 
            return HttpResponse("ajax is done!")