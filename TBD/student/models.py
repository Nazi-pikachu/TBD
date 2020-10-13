from django.db import models

# Create your models here.


class Notification_Student(models.Model):
    id = models.IntegerField(primary_key=True)
    # Student_ID=
    Message = models.CharField(max_length=1000)
    Created = models.DateField()
    Updated = models.DateField()


def __str__(self):
    return self.id
