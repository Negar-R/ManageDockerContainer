import docker

from rest_framework import serializers

from ManageDockerContainer.docker import docker_client
from .models import App, AppContainerHistory, ContainerStatusEnum


class ManageAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["id", "name", "image", "command", "envs", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AppContainerHistorySerializer(serializers.ModelSerializer):
    app = serializers.CharField(source="app.name")
    status = serializers.SerializerMethodField()

    def get_status(self, container_history) -> ContainerStatusEnum:
        container = docker_client.containers.get(container_history.container_short_id)
        return (
            ContainerStatusEnum.RUNNING.value
            if container.status in ["created", "running", "restarting"]
            else ContainerStatusEnum.FINISHED.value
        )

    class Meta:
        model = AppContainerHistory
        fields = "__all__"
