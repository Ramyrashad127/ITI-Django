# Generated by Django 5.1 on 2024-08-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_comment_task_delete_todo_comment_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(help_text='Enter the title of the task', max_length=100),
        ),
    ]
