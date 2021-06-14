from rest_framework.serializers import HyperlinkedModelSerializer
from api.models import Todo

class TodoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ["url", "id", "name", "description", "status"]