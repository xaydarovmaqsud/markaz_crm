from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from account.serializer import UserSerializer
from account.models import User,UserTag

class StudentViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = User.objects.filter(id__in=[i.user.id for i in UserTag.objects.filter(tag__name='student')])
    serializer_class = UserSerializer

    def get_queryset(self):
        self.request.GET.get
        return User.objects.filter(id__in=[i.user.id for i in UserTag.objects.filter(tag__name='student')])

class TeacherViewSet(ModelViewSet):
    queryset = User.objects.filter(id__in=[i.user.id for i in UserTag.objects.filter(tag__name='teacher')])
    serializer_class = UserSerializer

