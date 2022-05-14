#from curses.ascii import HT
from ast import Pass
import email
from email.message import EmailMessage
from multiprocessing import context
from sre_constants import SUCCESS
from unittest import result
from urllib import response
#from django.contrib import settings
from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse , StreamingHttpResponse ,  HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail , EmailMessage
import InscriptionEtudiant
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.conf import settings
# from InscriptionEtudiant.models import Etudiant
from .forms import *
from .models import *
from . camera import VideoCamera
import os
import cv2
import posixpath
import time

import threading

from django.contrib.auth import authenticate , login , logout
# pour bloque l'acces a n'import quel page
from django.contrib.auth.decorators import login_required,user_passes_test
# import requests

# from .forms import CreatNewUser
from .decorators import allowedUsers , forAdmins
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile


############################################TEST########################
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'InscriptionEtudiant/index.html')



#for showing signup/login button for teacher
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'InscriptionEtudiant/adminclick.html')


#for showing signup/login button for teacher
def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'InscriptionEtudiant/teacherclick.html')


#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'InscriptionEtudiant/studentclick.html')





def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'InscriptionEtudiant/adminsignup.html',{'form':form})




def student_signup_view(request):
    form1=StudentUserForm()
    form2=StudentExtraForm()
    mydict={'form1':form1,'form2':form2}

    if request.method=='POST':
        print(request.POST,'FORM')
        form1=StudentUserForm(request.POST)
        form2=StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            f2 = form2.save(commit=False)
            f2.image = f'{request.POST.get("username")}/{request.POST.get("username")}.jpg'
            f2.save()
            form1.save()
            print('saved')
            # f1=form1.save(commit=False)
            # f1.set_password(user.password)
            # f1.save()
            # user.save()
            # form2.save(commit=False)
            # f2.user=user
            # user2=f2.save()
      
            
            print('***************************************************')

   
        return HttpResponseRedirect('studentlogin')
    return render(request,'InscriptionEtudiant/studentsignup.html',context=mydict)


def teacher_signup_view(request):
    form1=forms.TeacherUserForm()
    form2=forms.TeacherExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.TeacherUserForm(request.POST)
        form2=forms.TeacherExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)

        return HttpResponseRedirect('teacherlogin')
    return render(request,'InscriptionEtudiant/teachersignup.html',context=mydict)






#for checking user is techer , student or admin
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_teacher(request.user):
        accountapproval=models.TeacherExtra.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('teacher-dashboard')
        else:
            return render(request,'InscriptionEtudiant/teacher_wait_for_approval.html')
    elif is_student(request.user):
        accountapproval=models.StudentExtra.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('student-dashboard')
        else:
            return render(request,'InscriptionEtudiant/student_wait_for_approval.html')



def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_cap(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def home_view(request):
    # Get file name from the registration interface
    dir_name = request.GET.get('username')
    path = os.getcwd()
    file_name = "InscriptionEtudiant\Attendance database"
    new_path = os.path.join(path, file_name)
    print(new_path)
    print(new_path, type(new_path),"---------")
    print(dir_name, type(dir_name),"######")
    # Creating a folder in the database by joining the paths together with the file name from the interface
    p = os.path.join(new_path, dir_name)
    os.mkdir(p)
    check_file = os.path.exists(p)
    if check_file == True:
        newPath = os.path.join(new_path, p)
        print(newPath)
        # Capture 10 images from a video feed and save them in the created directory
        camera = cv2.VideoCapture(0)
        time.sleep(10)
        for i in range(10):
            return_value, image = camera.read()
            v = os.path.join(newPath, dir_name)
            cv2.imwrite(v + str(i) + '.jpg', image)
        del(camera)
    return render(request, "index.html")

def take_attendance(request):
    return render(request, "Menu.html")


        

def capture(request):
    username = request.POST.get('name')

    image_path = f"{os.getcwd()}\InscriptionEtudiant\Attendance database\{username}"
    if not os.path.isdir(image_path):
        os.mkdir(image_path)

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    image_path = f"{os.getcwd()}\InscriptionEtudiant\Attendance database\{username}\{username}.jpg"
    image_path = image_path.replace("\\","\\\\")
    return_value, image = camera.read()
    cv2.imwrite(image_path, image)
    del(camera)
    
    return HttpResponse('scaner closed')