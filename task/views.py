from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, DestroyAPIView

from task.models import Task
from task.serializers import TaskSerializer


class TasksList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetails(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreate(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDelete(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
