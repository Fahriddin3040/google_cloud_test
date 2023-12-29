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
	department = serializers.SerializerMethodField(method_name="get_departments", read_only=True)

	def get_departments(self, obj):
		return Department.objects.filter(department=obj.department)

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
