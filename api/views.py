from api.models import Todo
from api.serializers import TodoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'todos': reverse('todo-list', request=request, format=format)
    })

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class Todos(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer