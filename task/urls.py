from django.urls import path

from task.views import TaskDetails, TasksList, TaskDelete, TaskCreate

urlpatterns = [
    path('', TasksList.as_view()),
    path('<int:pk>/', TaskDetails.as_view()),
    path('create/', TaskCreate.as_view()),
    path('delete/<int:pk>/', TaskDelete.as_view()),
]
