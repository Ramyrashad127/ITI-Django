from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks/<int:cat_id>', views.cat_detail, name='cat_detail'),
    path('task/<int:task_id>', views.task_detail, name='task_detail'),
    path('state/<str:state>', views.task_state, name='task_state'),
]