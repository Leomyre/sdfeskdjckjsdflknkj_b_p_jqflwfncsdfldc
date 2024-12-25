from django.contrib import admin
from .models import Project, Contact, Skill, Users  # Importez vos modèles

# Enregistrez vos modèles dans l'admin
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Users)
