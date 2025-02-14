# models.py
from django.db import models

class PageView(models.Model):
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Page Views: {self.view_count}"
