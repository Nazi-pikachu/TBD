from django.db import models

# Create your models here.


class Student_Table(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # profile_pic =
    password = models.CharField(max_length=100)
    created = models.DateField()
    updated = models.DateField()
    address = models.CharField(max_length=500)
    course_id = models.IntegerField()


class Staff_Table(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # profile_pic =
    password = models.CharField(max_length=100)
    created = models.DateField()
    updated = models.DateField()
    address = models.CharField(max_length=500)


class HOD_ADMIN(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class COURSE_TABLE(models.Model):
    id = models.IntegerField(primary_key=True)
    Course_Name = models.CharField(max_length=100)
    created = models.DateField()
    updated = models.DateField()


class LEAVE_TABLE(models.Model):
    id = models.IntegerField(primary_key=True)
    # Student_Staff_ID=
    # IS_STAFF =
    # STATUS =
    Leave_Date = models.DateField()
    Created = models.DateField()
    Updated = models.DateField()


class Feedback_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    # Student_ID=
    Message = models.CharField(max_length=1000)
    Created = models.DateField()
    Updated = models.DateField()

    def __str__(self):
        return self.title
