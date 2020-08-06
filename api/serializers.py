from rest_framework import serializers
from .models import Task


class TaskDetailSerializer(serializers.ModelSerializer):
	"""Serializer for task object"""
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Task
		fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
	"""Serializer for task object"""

	class Meta:
		model = Task
		fields = ['title', 'status', 'priority', 'due_date', 'owner']