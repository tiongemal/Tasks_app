from django.urls import path
from . import views

urlpatterns = [

        path('', views.index, name='index'),
        path('tasks/', views.show_tasks, name='tasks'),
        path('add', views.add_task, name='add_task'),
        path('complete/<int:task_id>', views.complete_task, name='complete')
]