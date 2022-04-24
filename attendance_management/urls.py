"""attendance_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('Homepage/', views.Homepage,name='Homepage'),
    path('Login/', views.Login,name='Login'),
    path('AboutUs/', views.AboutUS,name='AboutUs'),
    path('ContactUs/', views.ContactUs,name='contactUs'),
    path('Takeattendance/', views.Takeattendance,name='Takeattendance'),
    path('studentpage/', views.studentpage,name='studentpage'),
    path('TeacherLogin/', views.TeacherLogin,name='TeacherLogin'),
    path('StudentLogin/', views.StudentLogin,name='StudentLogin'),
    path('AdminPage/', views.AdminPage,name='AdminPage'),
     path('AddStudent/', views.AddStudent,name='AddStudent'),
]
