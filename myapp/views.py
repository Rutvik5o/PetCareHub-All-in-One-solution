from asyncio import AbstractEventLoopPolicy

from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.utils.termcolors import color_names
from django.core.paginator import Paginator

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

    fetchdata = vetRegisterDB.objects.all()

    context = {
        "vetdis" : fetchdata
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

    data = userRegisterDB.objects.filter(id=userid).values('Address').first()
    address = data.get('Address')  #store thte address


    print(address)

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
    data.status = "Rejected"
    data.save()
    return redirect("/manageAppoint")


def UserAppointment(request):

    userid = request.session["log_id"]
    user_name = request.session["log_name"]

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



