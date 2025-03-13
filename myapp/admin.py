from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(userRegisterDB)
class showUserRegisterData(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password','Address','Gender','PhoneNo','TimeStamp']

@admin.register(vetRegisterDB)
class showVetRegisterData(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password','Photo','vet_photo','Gender','Phone','LicenseFile','Address','Specialization','YearsOfExperience','ClinicName','TimeStamp']

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
    list_display = ['id','userid','vetid','petname','petphoto','pet_photo','breed','age','symptoms','status','dateofappo','timeofappo']

