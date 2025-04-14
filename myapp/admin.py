from django.contrib import admin
from .models import *
#for report
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# Register your models here.


#report function
def export_to_pdf(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['id','userid','appointmentid','amount','status','razorpay_order_id']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.id, obj.userid, obj.appointmentid,obj.amount, obj.status, obj.razorpay_order_id])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"

@admin.register(userRegisterDB)
class showUserRegisterData(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password','Address','Gender','PhoneNo','TimeStamp']
    list_filter = ['TimeStamp']

@admin.register(vetRegisterDB)
class showVetRegisterData(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password','Photo','vet_photo','Price','Gender','Phone','LicenseFile','Address','Specialization','YearsOfExperience','ClinicName','TimeStamp']
    list_filter = ['TimeStamp']

@admin.register(shelterDB)
class showShelterData(admin.ModelAdmin):
    list_display = ['id','shelterName','shelterEmail','shelterImage','shelter_photo','shelterContact','shelterAddress','shelterLocationUrl','TimeStamp']
    list_filter = ['TimeStamp']

@admin.register(petCategoryDB)
class showPetCategoryData(admin.ModelAdmin):
    list_display = ['id','petCategory']

@admin.register(petDB)
class showPetTable(admin.ModelAdmin):
    list_display=['id','petName','petImage','pet_photo','petDescription','petAge','petBreed','petCategory','ShelterId','PetAddTimeStamp']
    list_filter = ['PetAddTimeStamp']

@admin.register(Appointment)
class AppointmentTable(admin.ModelAdmin):
    list_display = ['id','userid','vetid','petname','petCategory','petphoto','pet_photo','breed','age','symptoms','status','location','dateofappo','timeofappo','TimeStamp']
    list_filter = ['TimeStamp']

@admin.register(Blog)
class BlogData(admin.ModelAdmin):
    list_display = ['id','blogTitle','blogImage','blog_photo','vetid','vetPhoto','Description','TimeStamp']
    list_filter = ['TimeStamp']

@admin.register(newsletter)
class lettershow(admin.ModelAdmin):
    list_display = ['id','email']

@admin.register(Payment)
class showpayment(admin.ModelAdmin):
    list_display = ['id','userid','appointmentid','amount','timestamp','status','razorpay_order_id']
    list_filter = ['timestamp']
    actions = [export_to_pdf]

@admin.register(reportFromVet)
class showreport(admin.ModelAdmin):
    list_display = ['id','appointmentid','vetid','report','Description','timestamp']
    list_filter = ['timestamp']


@admin.register(WithdrawVet)
class ShowVetWithdraw(admin.ModelAdmin):
    list_display = ['appointmentid','vetid','account_holder_name','account_number','bank_name','ifsc_code','withdrawStatus']

