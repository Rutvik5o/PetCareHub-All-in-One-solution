from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class userRegisterDB(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Password = models.CharField(max_length=40)
    Address = models.TextField()
    Gender = models.CharField(max_length=10)
    PhoneNo = models.BigIntegerField()
    TimeStamp = models.DateTimeField(auto_now_add=True)

class vetRegisterDB(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Password = models.CharField(max_length=40)
    Photo = models.ImageField(upload_to='photos')
    Gender = models.CharField(max_length=10)
    Phone = models.BigIntegerField()
    LicenseFile = models.FileField(upload_to='files',default=None,max_length=250)
    Address = models.TextField()
    Specialization = models.CharField(max_length=20)
    YearsOfExperience = models.IntegerField()
    ClinicName = models.CharField(max_length=60)
    TimeStamp = models.DateTimeField(auto_now_add=True)

    def vet_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Photo.url))