from django.db import models

# Create your models here.
class StudentRegisteration(models.Model):
    student_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_mail = models.EmailField()
    student_exam_pass = models.BooleanField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username