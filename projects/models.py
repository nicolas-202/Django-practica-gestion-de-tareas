from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.db.models.functions import Now, TruncDay


class Project(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    delivery_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            # Implementación futura para postgres
            # models.CheckConstraint(
            #     condition=Q(delivery_date__gte=TruncDay(Now())),
            #     name="delivery_date_not_before_today"
            # ),
            models.UniqueConstraint(
                fields=["owner","name"],
                name="unique_project_per_owner"
            )
        ]
    def clean(self):
        if self.delivery_date and self.delivery_date < timezone.localdate():
            raise ValidationError("La fecha de entrega debe ser una fecha futura")
        return super().clean()
    def __str__(self):
        return self.name
    def remaining_days(self):
        remaining = self.delivery_date - timezone.now().date()
        return remaining.days

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            # Implementación futura para postgres
            # models.CheckConstraint(
            #     condition=Q(due_date__gte=TruncDay(Now())),
            #     name="due_date_not_before_today"
            # ),
            models.UniqueConstraint(
                fields=["project","title"],
                name="unique_task_per_project"
            )
        ]
    def clean(self):
        if self.due_date and self.due_date < timezone.localdate():
            raise ValidationError("La fecha de entrega debe ser una fecha futura")
        return super().clean()
    def __str__(self):
        return self.title
    def remaining_days(self):
        remaining = self.due_date - timezone.now().date()
        return remaining.days