from django.contrib import admin
from .models import SUBJECT_TABLE
from .models import Notification_Staff
from .models import Attendance_report
from .models import Attendance_Table

# Register your models here.
admin.site.register(SUBJECT_TABLE)
admin.site.register(Notification_Staff)
admin.site.register(Attendance_Table)
admin.site.register(Attendance_report)