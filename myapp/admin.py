from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(userRegisterDB)
class showUserRegisterData(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password','Address','Gender','PhoneNo','TimeStamp']

@admin.register(vetRegisterDB)
class showVetRegisterData(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password','Photo','vet_photo','Price','Gender','Phone','LicenseFile','Address','Specialization','YearsOfExperience','ClinicName','TimeStamp']

@admin.register(shelterDB)
class showShelterData(admin.ModelAdmin):
    list_display = ['id','shelterName','shelterEmail','shelterImage','shelter_photo','shelterContact','shelterAddress','shelterLocationUrl','TimeStamp']

@admin.register(petCategoryDB)
class showPetCategoryData(admin.ModelAdmin):
    list_display = ['id','petCategory']


@admin.register(petDB)
class showPetTable(admin.ModelAdmin):

    list_display=['id','petName','petImage','pet_photo','petDescription','petAge','petBreed','petCategory','ShelterId','PetAddTimeStamp']


@admin.register(Appointment)
class AppointmentTable(admin.ModelAdmin):
    list_display = ['id','userid','vetid','petname','petCategory','petphoto','pet_photo','breed','age','symptoms','status','location','dateofappo','timeofappo','TimeStamp']

@admin.register(Blog)
class BlogData(admin.ModelAdmin):
    list_display = ['id','blogTitle','blogImage','blog_photo','vetid','vetPhoto','Description','TimeStamp']

@admin.register(newsletter)

class lettershow(admin.ModelAdmin):

    list_display = ['id','email']

@admin.register(Payment)

class showpayment(admin.ModelAdmin):

    list_display = ['id','userid','appointmentid','amount','timestamp','status','razorpay_order_id']

@admin.register(reportFromVet)

class showreport(admin.ModelAdmin):

    list_display = ['id','appointmentid','vetid','report','Description','timestamp']