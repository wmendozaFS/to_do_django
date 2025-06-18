from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [

    # Crear una tarea
    path('create/', views.task_create, name='task_create'),

    # Recuperar lista de tareas
    path('', views.task_list, name='task_list'),

    # Recuperar un objeto tarea individual
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),

    # Actualizar una tarea
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),

    # Eliminar una tarea
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
]