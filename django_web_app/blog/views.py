from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.staticfiles.views import serve
from django.db.models import Q
from django.contrib import messages


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def search(request):
    template='blog/home.html'
    query = request.GET.get('q')
    
    if query:
        result = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(author__username__icontains=query) | 
            Q(content__icontains=query)
        ).filter(is_public=True)
    else:
        result = Post.objects.filter(is_public=True)
    
    context = {'posts': result}
    return render(request, template, context)

def getfile(request):
    return serve(request, 'File')

@login_required
def user_search(request):
    """Search for users to share files with"""
    query = request.GET.get('q', '')
    users = []
    
    if query:
        users = User.objects.filter(
            Q(username__icontains=query) | 
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query)
        ).exclude(id=request.user.id)[:10]
    
    context = {
        'users': users,
        'query': query
    }
    return render(request, 'blog/user_search.html', context)

@login_required
def share_file(request, post_id):
    """Share a file with specific users"""
    post = get_object_or_404(Post, id=post_id, author=request.user)
    
    if request.method == 'POST':
        user_ids = request.POST.getlist('users')
        users = User.objects.filter(id__in=user_ids)
        
        for user in users:
            post.shared_with.add(user)
        
        messages.success(request, f'File shared with {len(users)} user(s)!')
        return redirect('post-detail', pk=post.id)
    
    # Get all users except the current user
    users = User.objects.exclude(id=request.user.id)
    already_shared = post.shared_with.all()
    
    context = {
        'post': post,
        'users': users,
        'already_shared': already_shared
    }
    return render(request, 'blog/share_file.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(is_public=True)


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Increment download count when viewing
        if self.request.user.is_authenticated:
            self.object.download_count += 1
            self.object.save()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file', 'is_public']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file', 'is_public']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
