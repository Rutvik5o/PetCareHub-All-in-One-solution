from asyncio import AbstractEventLoopPolicy
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.utils.termcolors import color_names
from django.core.paginator import Paginator
import razorpay
from django.conf import settings

from .models import *
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def servicepage(request):
    return render(request,"service-single.html")

def blogpage(request):
    fetchdata = Blog.objects.all().order_by('-TimeStamp')  # Order by latest blogs

    # Apply pagination
    paginator = Paginator(fetchdata, 3)  # Show 6 blogs per page
    page_number = request.GET.get('page')
    page_data = paginator.get_page(page_number)

    context = {
        "data": page_data
    }
    return render(request, "blog.html", context)

def loginpage(request):
    return render(request,"login.html")

def vetLoginpage(request):
    return render(request,"vetLogin.html")

def registerpage(request):
    return render(request,"register.html")

def vetRegisterpage(request):
    return render(request,"vetRegister.html")

def blogsinglepage(request,id):

   fetchdata =Blog.objects.get(id=id)

   context = {
      "fetchsingle": fetchdata
    }


   return render(request,"blog-single.html",context)

def shopsingelpage(request):
    return render(request,"shop-single.html")

def vetdiscoverpage(request):
    fetchdata = vetRegisterDB.objects.all().order_by('-id')  # Fetch all vets, latest first

    # Apply pagination
    paginator = Paginator(fetchdata, 8)  # Show 8 veterinarians per page
    page_number = request.GET.get('page')
    page_data = paginator.get_page(page_number)

    context = {
        "vetdis": page_data
    }
    return render(request,"vetdiscover.html",context)


def forgetpass(request):
    return render(request,"forgot-password.html")


def getadoption(request):
    fetchpet = petDB.objects.all().order_by('-id')  # Fetch pets, latest first

    # Apply pagination
    paginator = Paginator(fetchpet, 6)  # Show 6 pets per page
    page_number = request.GET.get('page')
    page_data = paginator.get_page(page_number)

    context = {
        "datapet": page_data
    }
    return render(request, "adoption.html", context)

def testPage(request):
    return render(request,"testimonial.html")

def aboutour(request):
    return render(request,"about.html")

def pricingpage(request):
    return render(request,"pricing.html")

#def errorpage(request,exception):
 #   return render(request,"404.html",status=404)




def fetchuserdata(request):
    #varialbe
    u_name = request.POST.get("uname")
    u_email = request.POST.get("uemail")
    u_password = request.POST.get("upassword")
    u_address = request.POST.get("uaddress")
    u_gender = request.POST.get("ugender")
    u_phone = request.POST.get("uphone")

    print(f'{u_name},{u_email},{u_password},{u_address},{u_gender},{u_phone}')

    # query
    userDataQuery = userRegisterDB(Name=u_name, Email=u_email, Password=u_password, Address=u_address, Gender=u_gender,
                                   PhoneNo=u_phone)
    userDataQuery.save()

    return render(request,"register.html")

def fetchvetdata(request):
    #variables
    v_name = request.POST.get("uname")
    v_email = request.POST.get("uemail")
    v_password = request.POST.get("upassword")
    v_photo = request.FILES["uphoto"]
    v_file = request.FILES["ufile"]
    v_gender = request.POST.get("ugender")
    v_phone = request.POST.get("uphone")
    v_price = request.POST.get('charges')
    v_address = request.POST.get("uaddress")
    v_specialization = request.POST.get("uspecialization")
    v_yearsofexp = request.POST.get("uyear")
    v_clinicname = request.POST.get("uclinicname")

    print(f'{v_name},{v_email},{v_password},{v_photo},{v_file},{v_gender},{v_phone},{v_address},{v_specialization},{v_yearsofexp},{v_clinicname}')

    # query
    vetDataQuery = vetRegisterDB(Name=v_name, Email=v_email, Password=v_password, Photo=v_photo, Gender=v_gender,
                                 Phone=v_phone, LicenseFile=v_file, Address=v_address, Specialization=v_specialization,
                                 YearsOfExperience=v_yearsofexp, ClinicName=v_clinicname,Price=v_price)
    vetDataQuery.save()

    return render(request,"vetRegister.html")

#to check userdata
def checklogindata(request):
    username = request.POST.get("uemail")
    userpassword = request.POST.get("upassword")

    try:
        userdata = userRegisterDB.objects.get(Email=username,Password=userpassword)
        print(userdata)
        print('success')
        request.session['log_id'] = userdata.id
        request.session['log_name'] = userdata.Name

        print("name in session=> ", request.session.get('log_name'))  # ✅ Use .get() to avoid KeyError

    except:
        print('fail')
        userdata = None



    if userdata is not None:
        print('success')


        return render(request,"index.html")
    else:
        print('Invalid Email or Password')
        messages.error(request,"Invalid Email or Password!!")


    return render(request,"login.html")

#to checkvetdata

def checkVetlogindata(request):
    vetemail = request.POST.get("vemail")
    vetpassword = request.POST.get("vpassword")



    try:
        vetdata = vetRegisterDB.objects.get(Email=vetemail,Password=vetpassword)
        print('success')
        print(vetdata)

        request.session['vet_log_id'] = vetdata.id
        request.session['vet_log_name'] = vetdata.Name
        request.session['vet_log_photo'] = vetdata.Photo.url
    except:
        print('fail')
        vetdata = None

    if vetdata is not None:
        print('success!!')
        return render(request,"vetHomePage.html")
    else:
        print('Invalid Email or Password')
        messages.error(request,"Invalid EMAIL or PASSWORD!!")

    return render(request,"vetLogin.html")

def singlepagepet(request,id): #for viewinng single page of pet

    fetchdata = petDB.objects.get(id=id)


    context = {
        "fetchsingle" : fetchdata
    }

    return render(request,"singlepetpage.html",context)

def vetsinglepage(request,id): #for viewinng single page of pet

    fetchdata = vetRegisterDB.objects.get(id=id)


    context = {
        "fetchsingle" : fetchdata
    }

    return render(request,"singlevetpage.html",context)


def gotoShelter(request):
    petid = request.POST.get("petid")


    pet = petDB.objects.get(id=petid)


    shelter = shelterDB.objects.get(id=pet.ShelterId.id)

    context = {
        "fetchsingle": shelter
    }

    return render(request, "singleshelter.html", context)


def vetAppoint(request):

    return render(request,"vetAppointment.html")


def logout(request): #user logout
    try:
        del request.session["log_id"]
        del request.session["log_name"]
    except:
        None
    return redirect("/")

def vetlogout(request): #vet logout
    try:
        del request.session["vet_log_id"]
        del request.session["vet_log_name"]
        del request.session["vet_log_photo"]
    except:
        None
    return redirect("/vetLogin")



def makeAppointment(request):
    vetid = request.POST.get("vetid")
    fetchcatdata = petCategoryDB.objects.all()
    print(vetid)
    context = {
        "vetid":vetid,
        "allcatdata": fetchcatdata
    }


    return render(request,"vetAppointment.html",context)



def appointmentRequest(request):
    userid = request.session["log_id"]
    vetid = request.POST.get("vetid")
    petname = request.POST.get("petname")
    petage = request.POST.get("petage")
    petCategory_id = request.POST.get("pc")
    petImage = request.FILES["petimage"]
    Breed = request.POST.get("breed")
    location = request.POST.get("updatedA")

    data = userRegisterDB.objects.filter(id=userid).values('Address').first()
    address = data.get('Address')  #store thte address

    if location:  # If ;pcatopm is not empty
        address = location  # Use the new address
    else:
        address = address  # Use the old address




    date = request.POST.get("date")
    time = request.POST.get("time")

    sym = request.POST.get("sym")

    status = request.POST.get("status")


    insertquery = Appointment(userid=userRegisterDB(id=userid), vetid=vetRegisterDB(id=vetid), petname=petname,
                              age=petage, symptoms=sym, breed=Breed, dateofappo=date, timeofappo=time,location=address,
                              petCategory=petCategoryDB(id=petCategory_id), petphoto=petImage,status=status)

    insertquery.save()

    print("data Stored Succsefully")

    return render(request,"vetAppointment.html")


def manageAppoint(request):

    vet_id = request.session["vet_log_id"]
    fetchdata = Appointment.objects.filter(vetid=vet_id)

    context = {

        "data" : fetchdata
    }

    return render(request,"manageAppointment.html",context)

def accept(request,id):
    data = Appointment.objects.get(id=id)
    data.status = "Approved"
    data.save()
    return redirect("/manageAppoint")


def reject(request,id):
    data = Appointment.objects.get(id=id)
    data.status = "Rejected"

    data.save()
    return redirect("/manageAppoint")


def UserAppointment(request):
    userid = request.session.get('log_id')
    user_name = request.session.get('log_name')


    fetchdata = Appointment.objects.filter(userid=userid)

    context = {
        "data": fetchdata
    }


    print(userid)
    print(user_name)

    return render(request,"UserManageAppointment.html",context)


def cancelappointment(request,id):

    data = Appointment.objects.get(id=id)

    data.delete()

    return redirect("/userManageAppointment")

def blogP(request):

    return render(request,"blogPost.html")

def fetcharticle(request):

    Title = request.POST.get("title")
    Image = request.FILES["blogimage"]
    vet_id = request.session["vet_log_name"]
    vet_photo = request.session['vet_log_photo']
    article = request.POST.get("art")

    print(Title)

    insertquery = Blog(blogTitle=Title,blogImage=Image,vetid=vet_id,Description=article,vetPhoto=vet_photo)
    insertquery.save()
    return render(request,"vetHomePage.html")



def showletter(request):

    email = request.POST.get("email")

    insertquery = newsletter(email=email)

    insertquery.save()

    return redirect("/")

def faq(request):

    return render(request,"faq.html")

def terms(request):

    return render(request,"terms.html")

def policy(request):

    return render(request,"privacy.html")

def team(request):

    return render(request,"team.html")

def Petcare2o(request):

    return render(request,"coming-soon.html")


def MakePayment(request, appointment_id):
    # Retrieve the appointment object
    appointment = Appointment.objects.get(id=appointment_id)

    # Check if the appointment is "Approved"
    if appointment.status != "Approved":
        messages.error(request, "Only approved appointments can be paid for.")
        return redirect("/appointment")

    # Fetch the price of the vet for this appointment
    vet_price = appointment.vetid.Price
    amount = int(vet_price * 100)  # Razorpay expects the amount in paise, so multiply by 100

    # Initialize Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))

    # Create a Razorpay order
    razorpay_order = client.order.create({
        "amount": amount,  # amount in paise
        "currency": "INR",
        "receipt": f"order_rcptid_{appointment.userid.id}",
        "payment_capture": "1",
    })

    # Create Payment object to store the payment details
    payment = Payment(
        userid=appointment.userid,
        appointmentid=appointment,
        amount=amount,
        razorpay_order_id=razorpay_order['id'],
    )

    payment.save()

    # Render the payment page with necessary details
    return render(request, "payment.html", {
        "razorpay_order_id": razorpay_order['id'],
        "amount": amount,
        "key": settings.RAZORPAY_KEY_ID,
        "currency": "INR",
    })




@csrf_exempt
def PaymentSuccess(request):
    if request.method == "POST":
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_signature = request.POST.get("razorpay_signature")

        # # Check if we received the necessary data
        # if not razorpay_order_id or not razorpay_payment_id or not razorpay_signature:
        #     messages.error(request, "Missing payment details!")
        #     return redirect("/userManageAppointment")

        # Verify the payment with Razorpay
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))

        # Prepare parameters to verify the payment signature
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
        }

        try:
            # Verify the payment signature
            # client.utility.verify_payment_signature(params_dict)

            # Retrieve the payment object from the database using the order ID
            payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)

            # Mark the payment as successful
            payment.status = "Success"
            payment.save()

            # Update the related appointment status
            appointmentid = payment.appointmentid.id
            print("id",appointmentid)
            fetchdata = Appointment.objects.get(id=appointmentid)
            fetchdata.status = "Paid"
            fetchdata.save()

            messages.success(request, "Payment Successful!")
            return redirect("/userManageAppointment")

        except razorpay.errors.SignatureVerificationError as e:
            messages.error(request, f"Payment verification failed! Error: {str(e)}")
            return redirect("/userManageAppointment")

        except Exception as e:
            messages.error(request, f"An error occurred! Error: {str(e)}")
            return redirect("/userManageAppointment")


def uploadReport(request,id):
    context = {
        "id":id
    }
    if request.method == "POST":
        vetid = request.session["vet_log_id"]
        reportdata = request.FILES['rfile']

        desc = request.POST.get('d')

        insertquery = reportFromVet(report=reportdata,Description=desc,appointmentid=Appointment(id=id),vetid=vetRegisterDB(id=vetid))

        insertquery.save()
    return render(request, "uploadReport.html", context)



def manageBlogpage(request):

    vet_id = request.session["vet_log_name"]
    print(vet_id)
    if not vet_id:
        return redirect("/vetLogin")  # redirect if session is missing
    data = Blog.objects.filter(vetid=vet_id)
    fetchdata = Blog.objects.all().order_by('-TimeStamp')  # Order by latest blogs

    # Apply pagination
    page_number = request.GET.get('page')
    paginator = Paginator(fetchdata, 3)  # Show 6 blogs per page
    page_data = paginator.get_page(page_number)


    context = {
        "data": page_data,
        "fetchdata":data
    }
    return render(request, "manageBlog.html", context)