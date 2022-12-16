import docker

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import App
from .serializers import ManageAppSerializer


class ManageAppView(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = ManageAppSerializer
