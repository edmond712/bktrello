from django.db import models

class Task(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    due_date = models.DateField()
    completed = models.BooleanField(
        default=False
    )
    paginate_by = 2

    def __str__(self):
        return self.title

