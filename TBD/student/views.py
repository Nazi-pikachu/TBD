from django.shortcuts import render
from .models import Notification_Student

# Create your views here.


def students(request):
    n_s = Notification_Student.objects.all()
    return render(request, 'student/students.html', {'n_s': n_s})
