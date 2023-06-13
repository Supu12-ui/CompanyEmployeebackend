from django.db import models

# Create your models here.
#creating you company models
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=58)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('NonIT','NonIT'),('MobilesPhone','MobilePhonr')))
    added_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

#employe model
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=20)
    about=models.TextField()
    position=models.CharField(max_length=20,choices=(('Software', 'software'),
                                                     ('HR','HR'), ('Testing','Testing')
                                                     ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)