from django.db import models
import datetime


class SUBJECT_TABLE(models.Model):

    id = models.IntegerField(primary_key=True)
    Subject_Name = models.CharField(max_length=100)

    # Staff_ID=

    Course_ID = models.CharField(max_length=100)
    created = models.DateField()
    updated = models.DateField()


class Notification_Staff(models.Model):

    id = models.IntegerField(primary_key=True)

    # STAFF_ID=

    message = models.CharField(max_length=1000)
    created = models.DateField()
    updated = models.DateField()


class Attendance_report(models.Model):

    PRESENT_CHOICES = (('P', 'Present'), ('A', 'Absent'))
    id = models.IntegerField(primary_key=True)

    # Student_ID=

    Attendance_ID = models.IntegerField()
    Status = models.CharField(max_length=1, choices=PRESENT_CHOICES)
    created = models.DateField()
    updated = models.DateField()


class Attendance_Table(models.Model):

    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.title
