from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from permissions.decorators.permission import has_permissions
from permissions.course import COURSE

from course.models import Course,TeacherCourse
from course.serializer import CourseSerializer
from group.serializer import GroupSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @has_permissions(permissions=[COURSE.VIEW])
    def retrieve(self, request, *args, **kwargs):
        instance:Course = self.get_object()
        serializer = CourseSerializer(instance)
        groups = instance.groups.all()
        groups_data = GroupSerializer(groups,many=True).data
        data = serializer.data
        data['groups'] = groups_data
        return Response(data)

    @has_permissions(permissions=[COURSE.DELETE,COURSE.VIEW])
    def destroy(self, request, *args, **kwargs):
        return super(CourseViewSet, self).destroy(self, request, *args, **kwargs)