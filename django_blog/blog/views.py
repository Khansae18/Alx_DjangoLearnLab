from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, comment, Tag
from .forms import PostForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView



# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


# View details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update post (only by author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Delete post (only by author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return redirect('post-detail', pk=post.pk)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        post = self.object.post
        return post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

def post_list(request):
    query = request.GET.get('q')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)  
        ).distinct()
    return render(request, 'blog/post_list.html', {'posts': posts})

def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = tag.posts.all()
    return render(request, 'blog/posts_by_tag.html', {'tag': tag, 'posts': posts})


class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Get the tag slug from the URL
        tag_slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(tags__slug=tag_slug).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get('tag_slug')
        context['tag'] = Tag.objects.get(slug=tag_slug)
        return context



    