from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from group.models import Group
from group.serializer import GroupSerializer

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
