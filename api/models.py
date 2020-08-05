from django.db import models


class Task(models.Model):
    """Task model"""
    TASK_STATUS = (
        ('open', 'Open'),
        ('in_process', 'In process'),
        ('resolved', 'Resolved'),
    )
    TASK_PRIORITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('now', 'Now'),
    )
    title = models.CharField(verbose_name="Title", max_length=200)
    created = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)
    due_date = models.DateField(verbose_name="Due date")
    description = models.TextField(verbose_name="Task description")
    status = models.CharField(verbose_name="Task status", max_length=10, choices=TASK_STATUS, default="Open")
    priority = models.CharField(verbose_name="Task priority", max_length=6, choices=TASK_PRIORITY)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        ordering = ['due_date']
