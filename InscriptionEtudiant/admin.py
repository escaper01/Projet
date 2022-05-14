from django.contrib import admin
from .models import *
from .models import Attendance,StudentExtra,TeacherExtra,Notice
#from .models import Image
# Register your models here.


# from .models import Etudiant
# admin.site.register(Etudiant)

# from .models import Image
# admin.site.register(Image)

# Register your models here. (by sumit.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra, TeacherExtraAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id','name','email','password')