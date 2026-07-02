from django.db import models
from django.utils import timezone
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    delivery_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    def remaining_days(self):
        remaining = self.delivery_date - timezone.now().date()
        return remaining.hours