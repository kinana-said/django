from django.urls  import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

from . import views 

router =DefaultRouter()
router.register ('tasks',TaskViewSet,basename='task')
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home_redirect'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_form, name='task_add'),  # إضافة مهمة جديدة
    path('tasks/<int:pk>/edit/', views.task_form, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('logout/', views.logout_view, name='logout'),
    # API URLs
   # path('api/tasks/', views.TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task-api-list'),
    #path('api/tasks/<int:pk>/', views.TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='task-api-detail'),
]

#handler404 = 'todo.views.custom_404'
#handler500 = 'todo.views.custom_500'
