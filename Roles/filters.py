from django_filters import rest_framework as filters
from .models import Role

class RoleFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    location = filters.CharFilter(lookup_expr='icontains')
    role_type = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Role
        fields = ['title', 'location', 'role_type']
