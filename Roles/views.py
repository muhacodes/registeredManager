from rest_framework import viewsets
from .models import Role
from .serializer import RoleSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'location', 'role_type']