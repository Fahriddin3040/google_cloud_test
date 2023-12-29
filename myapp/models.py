from django.db import models


class CourSeChoices(models.IntegerChoices):
	FIRST = 1
	SECOND = 2
	THIRD = 3
	FIFTH = 4


class Teacher(models.Model):
	class Roles(models.IntegerChoices):
		TEACHER = (1, "Учитель")
		HEAD_OF_DEPARTMENT = (2, "Декан")
		HEAD_OF_FACULTY = (3, "Заведующий кафедрой")

	full_name = models.CharField(max_length=50, verbose_name="ФИО")
	email = models.EmailField(blank=True, null=True, verbose_name="Адрес эл.почты")
	phone_number = models.IntegerField(blank=True, null=True, verbose_name="Номер телефона")
	faculty = models.ForeignKey(
		"myapp.Faculty",
		on_delete=models.CASCADE,
		verbose_name="Факультет",
		related_name="teacher_faculty"
	)
	department = models.ForeignKey(
		"myapp.Department",
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		verbose_name="Кафедра",
		related_name="teacher_department"
	)
	role = models.SmallIntegerField(choices=Roles.choices, verbose_name="Роль")

	def __str__(self):
		return self.full_name

	class Meta:
		verbose_name = "Учитель"
		verbose_name_plural = "Учителя"


class Student(models.Model):
	full_Name = models.CharField(max_length=50, verbose_name="ФИО")
	phone_number = models.IntegerField(verbose_name="Номер телефона")
	speciality = models.ForeignKey(
		"myapp.Speciality",
		on_delete=models.CASCADE,
		related_name="student_speciality",
		verbose_name="Специальность",
	)
	course = models.SmallIntegerField(choices=CourSeChoices.choices, verbose_name="Год учёбы")

	def __str__(self):
		return self.full_Name

	class Meta:
		verbose_name = "Студент"
		verbose_name_plural = "Студенты"


class Faculty(models.Model):

	title = models.CharField(max_length=50, unique=True, verbose_name="Название")
	head = models.ForeignKey(
		"myapp.Teacher",
		on_delete=models.CASCADE,
		verbose_name="Декан",
		related_name="faculty_head",
		blank=True,
		null=True
	)
	departments = models.ManyToManyField(
		"myapp.Department",
		related_name="faculty_departments",
		verbose_name="Кафедры",
		blank=True,
		null=True
	)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Факультет"
		verbose_name_plural = "Факультеты"


class Department(models.Model):

	title = models.CharField(max_length=75, unique=True, verbose_name="Декан")
	head = models.ForeignKey(
		"myapp.Teacher",
		on_delete=models.CASCADE,
		related_name="department_head",
		verbose_name="Заведующий кафедры",
		blank=True,
		null=True,
	)

	def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
		self.head.faculty = self
		super().save(
			force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields
		)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Кафедра"
		verbose_name_plural = "Кафедры"


class Speciality(models.Model):
	class GroupChoices(models.TextChoices):
		TA = "Ta"
		TB = "Tб"
		TC = "Тв"
		RA = "Ра"
		RB = "Рб"
		RC = "Рв"

	group = models.CharField(max_length=5, choices=GroupChoices.choices, verbose_name="Группа")
	curator = models.ForeignKey("myapp.Teacher", on_delete=models.CASCADE, verbose_name="Куратор", null=True, blank=True)
	title = models.CharField(max_length=50, unique=True, verbose_name="Название")
	code_name = models.IntegerField(unique=True, verbose_name="Кодовое название")
	department = models.ForeignKey(
		"myapp.Department",
		on_delete=models.CASCADE,
		related_name="speciality_department",
		verbose_name="Кафедра"
	)
	course = models.SmallIntegerField(choices=CourSeChoices.choices)

	def __str__(self):
		return f"{self.title} - {self.course}_{self.code_name}"



