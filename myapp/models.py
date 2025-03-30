from encodings.punycode import selective_find

from django.db import models
from django.utils.safestring import mark_safe
import re
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
    Price = models.IntegerField(default=500)
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
    shelterLocationUrl = models.TextField(null=True)
    TimeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shelterName

    def shelter_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.shelterImage.url))

    # def save(self, *args, **kwargs):
    #     if self.shelterLocationUrl and "google.com/maps/place" in self.shelterLocationUrl:
    #         # Extract Coordinates
    #         match = re.search(r'@(-?\d+\.\d+,-?\d+\.\d+)', self.shelterLocationUrl)
    #         if match:
    #             lat, lng = match.group(1).split(',')
    #             self.shelterLocationUrl = f"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d0!2d{lng}!3d{lat}"
    #
    #     super(shelterDB, self).save(*args, **kwargs)

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
    status = models.CharField(max_length=30,null=True,default="Pending")
    dateofappo = models.DateField()
    timeofappo = models.TimeField()
    TimeStamp =models.DateTimeField(auto_now=True)
    location = models.TextField(null=True,default="")

    def pet_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.petphoto.url))

    def __str__(self):
        return f"ApID - {self.id}"




class Blog(models.Model):

    blogTitle = models.CharField(max_length=30)
    blogImage = models.ImageField(upload_to='photos')
    vetid = models.CharField(max_length=30)
    vetPhoto = models.ImageField(upload_to='photos',null=True,default="")
    Description = models.TextField()
    TimeStamp = models.DateTimeField(auto_now=True)

    def blog_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.blogImage.url))


class newsletter(models.Model):
    email = models.CharField(max_length=30)


class Payment(models.Model):
    userid = models.ForeignKey(userRegisterDB, on_delete=models.CASCADE)
    appointmentid = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default="Pending")  # Can be Pending, Success, Failed
    razorpay_order_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Payment {self.id} - {self.status}"


class reportFromVet(models.Model):
    appointmentid = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    vetid = models.ForeignKey(vetRegisterDB, on_delete=models.CASCADE)
    report = models.FileField(upload_to='files',max_length=250)
    Description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"by {self.appointmentid.userid.Name}"




class GetIntoTouch(models.Model):

    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.TextField()



class WithdrawVet(models.Model):

    appointmentid = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    vetid = models.ForeignKey(vetRegisterDB,on_delete=models.CASCADE)
    account_holder_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=11)
    withdrawStatus = models.CharField(max_length=30,null=True,default="Pending")

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_holder_name} - {self.bank_name}"




