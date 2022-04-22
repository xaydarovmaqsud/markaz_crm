from rest_framework import routers
from course.views import CourseViewSet
from account.views import StudentViewSet, TeacherViewSet
from group.views import GroupViewSet
router:routers.DefaultRouter = routers.DefaultRouter()
router.register('course',CourseViewSet,basename='course')
router.register('student',StudentViewSet,basename='student')
router.register('teacher',TeacherViewSet,basename='teacher')
router.register('group',GroupViewSet,basename='group')