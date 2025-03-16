from django.shortcuts import render , redirect
from django.utils.termcolors import color_names

from .models import *
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def servicepage(request):
    return render(request,"service-single.html")

def blogpage(request):
    return render(request,"blog.html")

def loginpage(request):
    return render(request,"login.html")

def vetLoginpage(request):
    return render(request,"vetLogin.html")

def registerpage(request):
    return render(request,"register.html")

def vetRegisterpage(request):
    return render(request,"vetRegister.html")

def blogsinglepage(request):
    return render(request,"blog-single.html")

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

    fetchpet = petDB.objects.all()

    context = {
        "datapet" : fetchpet
    }
    return render(request,"adoption.html",context)

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
    except:
        print('fail')
        vetdata = None

    if vetdata is not None:
        print('success!!')
        return render(request,"index.html")
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

def vetAppoint(request):

    return render(request,"vetAppointment.html")


def logout(request):
    try:
        del request.session["log_id"]
        del request.session["log_name"]
    except:
        None
    return redirect("/")


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

    date = request.POST.get("date")
    time = request.POST.get("time")

    sym = request.POST.get("sym")
    if request.session["log_id"] == "":
        print("cant")
    else:
        status = True


    insertquery = Appointment(userid=userRegisterDB(id=userid), vetid=vetRegisterDB(id=vetid), petname=petname,
                              age=petage, symptoms=sym, breed=Breed, dateofappo=date, timeofappo=time,
                              petCategory=petCategoryDB(id=petCategory_id), petphoto=petImage,status=status)

    insertquery.save()

    print("data Stored Succsefully")

    return render(request,"vetAppointment.html")


def manageAppoint(request):
    return render(request,"manageAppointment.html")
