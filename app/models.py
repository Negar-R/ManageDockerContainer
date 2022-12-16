from django.db import models


class App(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=255)
    command = models.CharField(max_length=255, null=True, blank=True)
    envs = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
