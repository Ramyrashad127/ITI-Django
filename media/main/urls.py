from django.contrib import admin
from django.urls import path
from django.urls import include
from .models import Profile, User, Post, Comment, Like
from .views import home ,comments, RegisterView, edit_profile
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('comments/<int:post_id>', comments, name='comments'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile',edit_profile,name='edit_profile' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
