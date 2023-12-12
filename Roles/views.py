from rest_framework import viewsets
from .models import Role
from .serializer import RoleSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoleFilter

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoleFilter
    # filterset_fields = ['title', 'location', 'role_type']