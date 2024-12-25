from rest_framework import serializers
from .models import Project, Skill, Contact, Users  # Ajout de Users

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'link']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'level']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'email', 'phone', 'github', 'facebook']  # Ajout du champ 'facebook'

class UsersSerializer(serializers.ModelSerializer):  # Ajout du serializer pour Users
    class Meta:
        model = Users
        fields = ['id', 'name', 'bio']  # Ajout du champ 'bio'
