from django.contrib import admin
from.models import CourseData

class AdminCourseData(admin.ModelAdmin):
    list_display = ['course_id','course_name','course_dur','course_fee','start_time','start_date','trainer_name','trainer_exp']


admin.site.register(CourseData,AdminCourseData)

