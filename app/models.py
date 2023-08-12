from django.db import models


class TaskItem(models.Model):
    COMPLETED = 'C'
    UNCOMPLETED = 'U'
    TASK_STATUS_CHOICES = [
        (COMPLETED, 'completed'),
        (UNCOMPLETED, 'not completed')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default=UNCOMPLETED)

    def __str__(self):
        return f'{self.title}'
