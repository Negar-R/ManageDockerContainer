import enum

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


class ContainerStatusEnum(enum.Enum):
    RUNNING = "running"
    FINISHED = "finished"


class AppContainerHistory(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    # As App object can be updated and it is possible to change its props, so it is required to consider
    # a new field for each of its props in this model.
    container_short_id = models.CharField(max_length=12, unique=True)
    container_name = models.CharField(max_length=255)
    container_image = models.CharField(max_length=255)
    container_command = models.CharField(max_length=255, null=True, blank=True)
    container_envs = models.JSONField(default=dict)
    container_logs = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.container_name


# Note: Generally, it would be better to save logs(history of changes) in file. for example use logging of django.
# But for now, we need to do some process on logs.e.g: Get the logs of one specific app(or do some filters).
# So it would be useful to use DB to store them.
