from rest_framework import serializers
from .models import Role  # Adjust the import according to your app structure


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'  # Or list specific fields like ['title', 'location', 'salary', ...]
