from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Profile, Like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .form import Create_user, ProfileForm

@login_required
def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    likes = Like.objects.all()
    context = {'posts': posts, 'comments': comments, 'likes': likes, 'user': request.user}
    return render(request, 'main/home.html', context)

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author=request.user)
    context = {'profile': profile, 'posts': posts, 'user' :request.user}
    return render(request, 'main/profile.html', context)

@login_required
def comments(request, post_id):
    comments = Comment.objects.filter(post=post_id)
    context = {'comments': comments, 'user': request.user}
    return render(request, 'main/comments.html', context)

class RegisterView(CreateView):
    form_class = Create_user
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response

def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'main/edit_profile.html', {'form': form})
