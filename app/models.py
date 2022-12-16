from rest_framework import serializers

from .models import App


class ManageAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["id", "name", "image", "command", "envs", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
