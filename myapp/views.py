from django.shortcuts import render
from rest_framework import viewsets
from .models import (
	Teacher,
	Student,
	Faculty,
	Department,
	Speciality
)
from .serializers import TeacherSerializer, StudentSerializer, FacultySerializer, DepartmentSerializer, \
	SpecialitySerializer


class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class FacultyViewSet(viewsets.ModelViewSet):
	queryset = Faculty.objects.all()
	serializer_class = FacultySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
	queryset = Speciality.objects.all()
	serializer_class = SpecialitySerializer
