from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(userRegisterDB)
class showUserRegisterData(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password','Address','Gender','PhoneNo','TimeStamp']

@admin.register(vetRegisterDB)
class showVetRegisterData(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password','Photo','Gender','Phone','LicenseFile','Address','Specialization','YearsOfExperience','ClinicName','TimeStamp']

@admin.register(shelterDB)
class showShelterData(admin.ModelAdmin):
    list_display = ['id','shelterName','shelterEmail','shelterContact','shelterAddress','shelterLocationUrl','TimeStamp']

@admin.register(petCategoryDB)
class showPetCategoryData(admin.ModelAdmin):
    list_display = ['id','petCategory']