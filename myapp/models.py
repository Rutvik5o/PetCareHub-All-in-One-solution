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

    def __str__(self):
        return self.Name

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

    vet_photo.allow_tags = True

    def __str__(self):
        return self.Name



class shelterDB(models.Model):
    shelterName = models.CharField(max_length=70)
    shelterEmail = models.EmailField()
    shelterContact = models.BigIntegerField()
    shelterAddress = models.TextField()
    shelterImage = models.ImageField(upload_to="photos",default="",null=True)
    shelterLocationUrl = models.URLField(blank=True,null=True)
    TimeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shelterName

    def shelter_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.shelterImage.url))

    shelter_photo.allow_tags = True


class petCategoryDB(models.Model):
    petCategory = models.CharField(max_length=20)

    def __str__(self):
        return self.petCategory


class petDB(models.Model):

    petName = models.CharField(max_length=30)
    petImage = models.ImageField(upload_to='photos')
    petDescription = models.TextField()
    petAge = models.IntegerField()
    petBreed = models.CharField(max_length=30)
    petCategory = models.ForeignKey(petCategoryDB,on_delete=models.CASCADE)
    ShelterId = models.ForeignKey(shelterDB,on_delete = models.CASCADE)
    PetAddTimeStamp = models.DateTimeField(auto_now_add=True)

    def pet_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.petImage.url))

    pet_photo.allow_tags = True


class Appointment(models.Model):
    userid = models.ForeignKey(userRegisterDB,on_delete=models.CASCADE)
    vetid = models.ForeignKey(vetRegisterDB,on_delete=models.CASCADE)
    petname = models.CharField(max_length=30)
    petphoto = models.ImageField(upload_to='photos')
    petCategory = models.ForeignKey(petCategoryDB,on_delete=models.CASCADE)
    breed = models.CharField(max_length=20)
    age = models.IntegerField()
    symptoms = models.CharField(max_length=20)
    status = models.BooleanField()
    dateofappo = models.DateField()
    timeofappo = models.DateTimeField(auto_now=True)

    def pet_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.petphoto.url))






