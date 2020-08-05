from rest_framework.generics import ListCreateAPIView

from api.models import Task
from api.serializers import TaskSerializer


class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
