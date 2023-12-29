# Generated by Django 5.0 on 2023-12-29 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(default=1, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_faculty', to='myapp.faculty', verbose_name='Факультет'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_head', to='myapp.teacher', verbose_name='Заведующий кафедры'),
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=75, unique=True, verbose_name='Декан'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='departments',
            field=models.ManyToManyField(related_name='faculty_departments', to='myapp.department', verbose_name='Кафедры'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_head', to='myapp.teacher', verbose_name='Декан'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='code_name',
            field=models.IntegerField(unique=True, verbose_name='Кодовое название'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='curator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher', verbose_name='Куратор'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speciality_department', to='myapp.department', verbose_name='Кафедра'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='group',
            field=models.CharField(choices=[('Ta', 'Ta'), ('Tб', 'Tb'), ('Тв', 'Tc'), ('Ра', 'Ra'), ('Рб', 'Rb'), ('Рв', 'Rc')], max_length=5, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.SmallIntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fifth')], verbose_name='Год учёбы'),
        ),
        migrations.AlterField(
            model_name='student',
            name='full_Name',
            field=models.CharField(max_length=50, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_speciality', to='myapp.speciality', verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_department', to='myapp.department', verbose_name='Кафедра'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Адрес эл.почты'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'Учитель'), (2, 'Декан'), (3, 'Заведующий кафедрой')], verbose_name='Роль'),
        ),
    ]