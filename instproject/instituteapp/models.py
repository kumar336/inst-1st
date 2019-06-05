from django.db import models
from multiselectfield import MultiSelectField


class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateField()
    feedback=models.TextField(max_length=1000)


class ContactData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()

    COURSES_CHOICES = (
        ('py','Python'),
        ('dj','Django'),
        ('ui','UI'),
        ('rest','REST API')
    )
    courses=MultiSelectField(max_length=100, choices= COURSES_CHOICES)

    SHIFT_CHOICES= (
        ('mng','Morning'),
        ('aftn','Afternoon'),
        ('evng','Evining'),
        ('night','Night')

    )
    shifts=MultiSelectField(max_length=100, choices= SHIFT_CHOICES)

    LOCATION_CHOICES= (
        ('hyd','Hydrabad'),
        ('bang','Banglore'),
        ('che','Chennai'),
        ('pune','Pune')
    )
    locations = MultiSelectField(max_length=200, choices= SHIFT_CHOICES)

    gender=models.CharField(max_length=200, choices=LOCATION_CHOICES)

    start_date = models.DateField(max_length=100)

class CourseData(models.Model):
    course_id=models.IntegerField()
    course_name=models.CharField(max_length=100)
    course_dur=models.IntegerField()
    course_fee=models.IntegerField()
    start_date=models.DateField(max_length=120)
    start_time=models.TimeField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.IntegerField()
