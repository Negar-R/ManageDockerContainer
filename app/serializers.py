import docker

from rest_framework import serializers

from .models import App, AppContainerHistory, ContainerStatus

client = docker.from_env()


class ManageAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["id", "name", "image", "command", "envs", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AppContainerHistorySerializer(serializers.ModelSerializer):
    app = serializers.CharField(source="app.name")
    status = serializers.SerializerMethodField()

    def get_status(self, container_history) -> ContainerStatus:
        container = client.containers.get(container_history.container_short_id)
        return (
            ContainerStatus.RUNNING.name
            if container.status in ["created", "running", "restarting"]
            else ContainerStatus.FINISHED.name
        )

    class Meta:
        model = AppContainerHistory
        fields = "__all__"
