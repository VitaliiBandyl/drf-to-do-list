from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
	"""Serializer for task object"""
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Task
		fields = '__all__'