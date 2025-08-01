from django.urls import path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [

    # Crear una tarea
    path('create/', views.task_create, name='task_create'),

    # Recuperar lista de tareas
    path('', views.task_list, name='task_list'),

    # Recuperar un objeto tarea individual
    path('<int:pk>/', views.task_detail, name='task_detail'),

    # Actualizar una tarea
    path('<int:pk>/update/', views.task_update, name='task_update'),

    # Eliminar una tarea
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),

]
