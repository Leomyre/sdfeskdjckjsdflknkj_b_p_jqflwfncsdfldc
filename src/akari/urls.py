from django.urls import path
from .views import ProjectViewSet, SkillViewSet, ContactViewSet, UsersViewSet  # Ajout de UsersViewSet

urlpatterns = [
    path('projects/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-list'),
    path('projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='project-detail'),
    
    path('skills/', SkillViewSet.as_view({'get': 'list', 'post': 'create'}), name='skill-list'),
    path('skills/<int:pk>/', SkillViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='skill-detail'),
    
    path('contacts/', ContactViewSet.as_view({'get': 'list', 'post': 'create'}), name='contact-list'),
    path('contacts/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='contact-detail'),
    
    path('users/', UsersViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),  # Ajout de la route pour Users
    path('users/<int:pk>/', UsersViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),  # Route pour un utilisateur spécifique
]
