from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

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
