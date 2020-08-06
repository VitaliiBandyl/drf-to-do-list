from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.permissions import IsOwnerOrReadOnly
from api.models import Task
from api.serializers import TaskDetailSerializer, TaskListSerializer


class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
