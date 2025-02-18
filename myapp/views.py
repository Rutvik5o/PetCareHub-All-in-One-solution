from django.shortcuts import render
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


def forgetpass(request):
    return render(request,"forgot-password.html")

def getadoption(request):
    return render(request,"adoption.html")

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
    v_address = request.POST.get("uaddress")
    v_specialization = request.POST.get("uspecialization")
    v_yearsofexp = request.POST.get("uyear")
    v_clinicname = request.POST.get("uclinicname")

    print(f'{v_name},{v_email},{v_password},{v_photo},{v_file},{v_gender},{v_phone},{v_address},{v_specialization},{v_yearsofexp},{v_clinicname}')

    # query
    vetDataQuery = vetRegisterDB(Name=v_name, Email=v_email, Password=v_password, Photo=v_photo, Gender=v_gender,
                                 Phone=v_phone, LicenseFile=v_file, Address=v_address, Specialization=v_specialization,
                                 YearsOfExperience=v_yearsofexp, ClinicName=v_clinicname)
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