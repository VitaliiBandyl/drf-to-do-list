from django.urls import path

from api import views

urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name="task-list"),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name="task-detail"),
]
