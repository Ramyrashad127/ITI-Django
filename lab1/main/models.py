from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length= 50 , unique=True)
    description = models.TextField(null = True)
    def __str__(self):
        return self.name

class Task(models.Model):
    db_table = 'task'
    State = [('pending', 'pending'), ('in progress', 'in progress'), ('completed', 'completed')]
    title = models.CharField(max_length=100, help_text='Enter the title of the task')
    description = models.TextField()
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)] , default=5)
    due_date = models.DateField(null=True)
    statous = models.CharField(max_length=20, choices=State, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updeted_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

 
class Comment(models.Model):
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    task = models.ForeignKey(Task , on_delete = models.CASCADE)
    def __str__(self):
        return "comment on " + self.task.title