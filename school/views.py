from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    for student in students:
        teachers = student.teacher.all()
        for teacher in teachers:
            print(teacher.name)
    context = {'students': students}



    return render(request, template, context)
