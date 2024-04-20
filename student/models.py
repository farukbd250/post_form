from django.db import models
GENDER_CHOICES = (
    ('',''),
    ('male', 'MALE'),
    ('female','FEMALE'),
    ('unspecified','UNSPECIFIED'),
    
)


# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=50)
    father_name= models.CharField(max_length=50)
    mother_name= models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone= models.CharField(max_length=15)
    present_address= models.CharField(max_length=200)
    permanent_address= models.CharField(max_length=200)
    state= models.CharField(max_length=25)
    date_of_birth=models.DateField()
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='')
    image=models.FileField(upload_to="photo/")
    def __str__(self):
        return self.name
    
class StudentForm(models.Model) :
    name= models.CharField(max_length=50)
    father_name= models.CharField(max_length=50)
    mother_name= models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone= models.CharField(max_length=15)
    address= models.CharField(max_length=200)
    image=models.FileField(upload_to="photo/")
    def __str__(self):
        return self.name
    
    