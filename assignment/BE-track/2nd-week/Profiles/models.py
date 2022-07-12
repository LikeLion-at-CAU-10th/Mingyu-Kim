from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 30, default = "홍길동", null = True, blank = True)
    age = models.IntegerField(default = 25, null = True, blank = True)
    school = models.CharField(max_length = 30, default="CAU", null = True, blank = True)
    major = models.CharField(max_length = 50, default= "CSE", null = True, blank = True)
    pup_date = models.DateField(auto_now_add = True)
