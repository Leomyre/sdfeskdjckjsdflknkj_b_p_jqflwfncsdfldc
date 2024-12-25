from rest_framework import viewsets
from .models import Project, Skill, Contact, Users  # Ajout de Users
from .serializers import ProjectSerializer, SkillSerializer, ContactSerializer, UsersSerializer  # Ajout de UsersSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # Si vous n'avez qu'un seul contact et voulez un seul objet dans la vue
    def get_queryset(self):
        return Contact.objects.all()[:1]  # Récupère uniquement le premier contact (s'il y en a un seul)

    def perform_update(self, serializer):
        # On met à jour le contact. Si vous avez qu'un seul contact, vous pouvez l'assurer de cette manière.
        serializer.save()

class UsersViewSet(viewsets.ModelViewSet):  # Ajout de la vue Users
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
