from rest_framework.response import Response
from todos.serializers import TodoSerializer
from .models import Todo
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action


class TodoViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = TodoSerializer

  def get_queryset(self):
    return Todo.objects.filter(author=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(author=self.request.user)

  @action(detail=True, methods=['patch'])
  def check(self, request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.check_todo()
    serializer = self.serializer_class(todo)
    return Response(serializer.data, status=status.HTTP_200_OK)
