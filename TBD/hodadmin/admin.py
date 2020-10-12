from django.contrib import admin
from .models import Student_Table
from .models import Staff_Table
from .models import HOD_ADMIN
from .models import COURSE_TABLE
from .models import LEAVE_TABLE
from .models import Feedback_Table


# Register your models here.
admin.site.register(Student_Table)
admin.site.register(Staff_Table)
admin.site.register(HOD_ADMIN)
admin.site.register(COURSE_TABLE)
admin.site.register(LEAVE_TABLE)
admin.site.register(Feedback_Table)
