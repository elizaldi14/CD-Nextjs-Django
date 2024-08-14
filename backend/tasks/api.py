#Importo todos los moedelos que ocupe

from rest_framework import viewsets, permissions
from tasks.models import Task
from tasks.seriallizers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# En esta clase propociona una api CRUD completa para el modelo Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        task = self.get_object()
        task.done = not task.done
        task.save()
        return Response({
            'status': 'task done' if task.done else 'task undone'

        }, status=status.HTTP_200_OK)
    