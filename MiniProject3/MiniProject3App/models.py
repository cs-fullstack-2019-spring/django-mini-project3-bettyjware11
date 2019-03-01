from django.db import models

# Create your models here.
class Timecard(models.Model):
    teacher_name = models.CharField(max_length=128)
    school = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    hours_taught = models.IntegerField()
    date_of_work = models.DateField()
    date_of_entry = models.DateTimeField()

    def __str__(self):
        return self.teacher_name
