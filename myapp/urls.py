from rest_framework.routers import DefaultRouter
from django.urls import path, include
from myapp import views
from .views import *

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'student', StudentViewSet, basename='student')
router.register(r'faculty', FacultyViewSet, basename='faculty')
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'speciality', SpecialityViewSet, basename='speciality')


urlpatterns = [
	path("", include(router.urls))
]