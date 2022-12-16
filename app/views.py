import docker

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import App, AppContainerHistory
from .serializers import ManageAppSerializer, AppContainerHistorySerializer


class ManageAppView(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializers = {
        "default": ManageAppSerializer,
        "run": AppContainerHistorySerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])

    @action(detail=True, methods=["get"], name="run")
    def run(self, request, *args, **kwargs):
        app = self.get_object()
        try:
            client = docker.from_env()
            container = client.containers.run(
                image=app.image,
                command=app.command,
                environment=app.envs,
                detach=True,
            )
            app_container_log = AppContainerHistory.objects.create(
                app=app,
                container_short_id=container.short_id,
                container_name=container.name,
                container_image=container.image,
                container_command=app.command,
                container_envs=app.envs,
                # TODO: Be more precise about the status
                container_status=container.status,
                container_logs=container.logs(),
            )
            serializer = self.get_serializer(app_container_log)
            return Response(
                serializer.data,
                headers={"message": "container runs successfully"},
            )
        except Exception as e:
            return Response(e)
