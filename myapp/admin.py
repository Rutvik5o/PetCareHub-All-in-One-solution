from django.contrib import admin
from .models import *
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER



def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{modeladmin.model.__name__}.csv"'

    writer = csv.writer(response)
    field_names = [field.name for field in modeladmin.model._meta.fields]
    writer.writerow(field_names)

    for obj in queryset:
        writer.writerow([smart_str(getattr(obj, field)) for field in field_names])

    return response


export_as_csv.short_description = "Export Selected as CSV file(Excel)"




def export_to_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name='TitleStyle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#d35400'),
    )


    title = Paragraph("PetCare Hub: Payment Report", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))  # Add space between title and table


    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#d35400')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),

        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#fef9e7')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#5D4037')),

        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#A1887F')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#fef9e7'), colors.HexColor('#fcefc7')])
    ])

    headers = ['ID', 'User ID', 'Appointment ID', 'Amount', 'Status', 'Razorpay Order ID']
    data = [
        [getattr(obj, field) for field in ['id', 'userid', 'appointmentid', 'amount', 'status', 'razorpay_order_id']]
        for obj in queryset
    ]

    t = Table([headers] + data, style=style)
    elements.append(t)

    doc.build(elements)

    return response

export_to_pdf.short_description = "Export to PDF"



class ExportActionMixin:
    actions = [export_as_csv]


# ---------------------------------------
# Admin Registrations
# ---------------------------------------

@admin.register(userRegisterDB)
class showUserRegisterData(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'Name', 'Email', 'Password', 'Address', 'Gender', 'PhoneNo', 'TimeStamp']
    list_filter = ['TimeStamp']
    actions = [export_as_csv]


@admin.register(vetRegisterDB)
class showVetRegisterData(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'Name', 'Email', 'Password', 'Photo', 'vet_photo', 'Price', 'Gender', 'Phone', 'LicenseFile','Address', 'Specialization', 'YearsOfExperience', 'ClinicName', 'TimeStamp']
    actions = [export_as_csv]
    list_filter = ['TimeStamp']

@admin.register(shelterDB)
class showShelterData(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'shelterName', 'shelterEmail', 'shelterImage', 'shelter_photo', 'shelterContact','shelterAddress', 'shelterLocationUrl', 'TimeStamp']
    actions = [export_as_csv]
    list_filter = ['TimeStamp']


@admin.register(petCategoryDB)
class showPetCategoryData(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'petCategory']
    actions = [export_as_csv]


@admin.register(petDB)
class showPetTable(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'petName', 'petImage', 'pet_photo', 'petDescription', 'petAge', 'petBreed', 'petCategory','ShelterId', 'PetAddTimeStamp']
    list_filter = ['PetAddTimeStamp']
    actions = [export_as_csv]


@admin.register(Appointment)
class AppointmentTable(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'userid', 'vetid', 'petname', 'petCategory', 'petphoto', 'pet_photo', 'breed', 'age','symptoms', 'status', 'location', 'dateofappo', 'timeofappo', 'TimeStamp']
    list_filter = ['TimeStamp']
    actions = [export_as_csv]


@admin.register(Blog)
class BlogData(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'blogTitle', 'blogImage', 'blog_photo', 'vetid', 'vetPhoto', 'Description', 'TimeStamp']
    list_filter = ['TimeStamp']
    actions = [export_as_csv]


@admin.register(newsletter)
class lettershow(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'email']
    actions = [export_as_csv]


@admin.register(Payment)
class showpayment(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'userid', 'appointmentid', 'amount', 'timestamp', 'status', 'razorpay_order_id']
    list_filter = ['timestamp']
    actions = [export_to_pdf, export_as_csv]


@admin.register(reportFromVet)
class showreport(admin.ModelAdmin, ExportActionMixin):
    list_display = ['id', 'appointmentid', 'vetid', 'report', 'Description', 'timestamp']
    list_filter = ['timestamp']
    actions = [export_as_csv]


@admin.register(WithdrawVet)
class ShowVetWithdraw(admin.ModelAdmin, ExportActionMixin):
    list_display = ['appointmentid', 'vetid', 'account_holder_name', 'account_number', 'bank_name', 'ifsc_code','withdrawStatus']
    actions = [export_as_csv]