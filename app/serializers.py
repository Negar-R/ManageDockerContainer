from rest_framework import serializers

from .models import App, AppContainerHistory


class ManageAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["id", "name", "image", "command", "envs", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AppContainerHistorySerializer(serializers.ModelSerializer):
    app = serializers.CharField(source="app.name")

    class Meta:
        model = AppContainerHistory
        fields = "__all__"
