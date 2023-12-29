from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
	class Meta:
		model = Faculty
		fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = '__all__'

class SpecialitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Speciality
		fields = '__all__'

