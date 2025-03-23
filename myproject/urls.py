"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path

import myapp.views
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexpage),
    path('service-single/',views.servicepage),
    path('blog/',views.blogpage),
    path('blogs/<int:id>',views.blogsinglepage),
    path('login/',views.loginpage),
    path('vetLogin/',views.vetLoginpage),
    path('register/',views.registerpage),
    path('fpass/',views.forgetpass),
    path('vetRegister/',views.vetRegisterpage),
    path('fetchuserdata',views.fetchuserdata),
    path('fetchvetdata',views.fetchvetdata),
    path('checklogindata',views.checklogindata),
    path('checkVetlogindata',views.checkVetlogindata),
    path('adopt/',views.getadoption),
    path('test/',views.testPage),
    path('about/',views.aboutour),
    path('price',views.pricingpage),
    path('ssp/',views.shopsingelpage),
    path('spp/<int:id>/',views.singlepagepet),
    path('svp/<int:id>/',views.vetsinglepage),
    path('vetdis/',views.vetdiscoverpage),
    path('makeAppointment',views.makeAppointment),
    path('logout/',views.logout),
    path('appointment',views.appointmentRequest),
    path('manageAppoint/',views.manageAppoint),
    path('manageBlog/',views.manageBlogpage),
    path('vlogout',views.vetlogout),
    path('accept/<int:id>',views.accept),
    path('reject/<int:id>',views.reject),
    path('gotoS',views.gotoShelter),
    path('userManageAppointment',views.UserAppointment),
    path('cancel/<int:id>',views.cancelappointment),
    path('blogpost',views.blogP),
    path('getarticle',views.fetcharticle),
    path('subscribe',views.showletter),
    path('faq',views.faq),
    path('terms',views.terms),
    path('pp',views.policy),
    path('team',views.team),
    path('soon',views.Petcare2o),
    path('payment/success/',views.PaymentSuccess),
    path('payment/<int:appointment_id>/', views.MakePayment),
    path('uploadr/<int:id>',views.uploadReport)



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#handler404='myapp.views.errorpage'


