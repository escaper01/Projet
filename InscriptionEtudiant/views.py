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
from InscriptionEtudiant.models import Etudiant
# from .forms import * 
# from .models import *
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
# from .recognize import Recognizer
# from django.http import HttpResponse
#from django.contrib.auth import login 
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from InscriptionEtudiant.models import Image



# def usersave(request):
#  if request.method== 'POST':        
#     User_name = request.POST["Username"]
#     User_phone = request.POST["Userphone"]
#     User_address = request.POST["Useraddress"]
#     pic = request.FILES["photo"]
#     User_info= UserDetails(User_name=User_name, User_phone=User_phone, User_address=User_address, User_pic= pic)
#     User_info.save()    
#     return render(request, 'accueil.html')

# def image_upload(request):
#     context = dict()
#     if request.method == 'POST':
#         print(request.POST)
#         #username = request.POST["username"]
#         # image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
#         image_path = request.POST["src"]
#         image = NamedTemporaryFile()
#         image.write(urlopen(path).read())
#         image.flush()
#         image = File(image)
#         name = str(image.name).split('\\')[-1]
#         name += '.jpg'  # store image in jpeg format
#         image.name = name
#         if image is not None:
            
           
#             obj = Image.objects.create(username=username, image=image)  # create a object of Image type defined in your model
#             obj.save()
#             context["path"] = obj.image.url  #url to image stored in my server/local device
#             context["username"] = obj.username
#         else :
#             return redirect('/')
#         return redirect('any_url')
#     return render(request, 'InscriptionEtudiant/index.html', context=context)  # context is like respose data we are se


# # @login_required(login_url='authen')
# def accueil(request):
#     return render(request , 'InscriptionEtudiant/accueil.html')

# #cette fonction peremet de supp les donnes
# def testt(request):
#     return render(request , 'InscriptionEtudiant/test.html')


# def forms(request):
#     return render(request , 'InscriptionEtudiant/test.html')


# # @notLoggedUsers
# def authen(request):

#         if request.method == 'POST':
#             username1 = request.POST.get('nom')
#             password = request.POST.get('password')
#             user = authenticate(request, nom=username1 , password=password)
#             if user is not None:
#                 login(request,user)
#             return redirect('accueil')
#         else:
#             messages.info(request, 'Credentials error')
#             return render(request, 'InscriptionEtudiant/okey.html') 
    
# #cette fonction ppermet d'afficher et ajouter les information
# # @notLoggedUsers(login_url = 'login')

# #@notLoggedUsers(login_url = 'login')
# #@allowedUsers(allowedGroups = ['admin'])
# #@forAdmins
# def add_show(request):
#      #etudiant = Etudiant.objects.all()
#      if request.method == 'POST':
#          fm = CreatNewUser(request.POST)
#          if fm.is_valid():
#              nm = fm.cleaned_data['nom']
#              pr = fm.cleaned_data['prenom']
#              el = fm.cleaned_data['email']
#              ph = fm.cleaned_data['phone']
#              ag = fm.cleaned_data['age']
#              ps = fm.cleaned_data['password']
#              cfps = fm.cleaned_data['confirm_password']
#              ps = fm.cleaned_data['pays']

#              reg = Etudiant(nom =nm ,prenom=pr , email=el , phone=ph , age=ag ,password = ps , confirm_password = cfps )
        


#              reg.save()
#              fm =  CreatNewUser()
#      else:
#          fm = CreatNewUser()
         
#      stud = Etudiant.objects.all()
#      return render(request , 'InscriptionEtudiant/addandshow.html',{'form':fm,  'stu':stud})

# #@allowedUsers(allowedGroups = ['admin'])
# #@forAdmins
# def update_data(request ,id):
#     if request.method == 'POST':
#         pi = Etudiant.objects.get(pk=id)
#         fm = CreatNewUser(request.POST, instance=pi)
#         if fm.is_valid:
#             fm.save()
#     else:
#         pi = Etudiant.objects.get(pk=id)
#         fm = CreatNewUser( instance=pi)

             
#     return render(request,'InscriptionEtudiant/updatestudent.html',{'form':fm})

# #@allowedUsers(allowedGroups = ['admin'])
# #@forAdmins
# def delete_date(request, id):
#          if request.method == 'POST':
#              pi = Etudiant.objects.get(pk=id)
#              pi.delete()
#              return  HttpResponseRedirect('/')

# def userLogout(request):
#     return render(request , 'InscriptionEtudiant/lgout.html')

# def updatestudent(request):
#     return render(request, 'InscriptionEtudiant/updatestudent.html')

# def main(request):
#     return render(request, 'InscriptionEtudiant/main.html')

# # @notLoggedUsers
# def inscri(request):
# #  if request.user.is_authenticated:
# #         return redirect('updatestudent')
# #  else:
#     # nom = request.POST['nom']
#     # prenom = request.POST['prenom']
#     # email = request.POST['email']
#     # phone = request.POST['phone']
#     # age = request.POST['age']
#     # password = request.POST['password']
#     # confirm_password = request.POST['confirm_password']
#     # pays = request.POST['pays']
#     # if User.objects.filter(email=email):
#     #     messages.error(request , 'Cet email a été déjà pris !')
#     # if not nom.isalnum():
#     #     messages.error(request , 'Le nom ne doit etre pas alphanumeric !')
#     # if not prenom.isalnum():
#     #     messages.error(request , 'Le prenom ne doit etre pas alphanumeric !')
#     form = CreatNewUser()
#     if request.method == 'POST':
#         details = {
#             'nom':request.POST['nom'],
#             'prenom':request.POST['prenom'],
#             'email':request.POST['email'],
#             'phone':request.POST['phone'],
#             'age':request.POST['age'],
#             'password':request.POST['password'],
#             'confirm_password':request.POST['confirm_password'],
#             'pays':request.POST['pays'],
#         }
#         form = CreatNewUser(request.POST)
#         if form.is_valid():    
#             # recaptcha_response = request.POST.get('g-recaptcha_response')
#             # data = {
#             #     'secret' : settings.GOOGLE_RECAPTCHA_SECRETY_KEY,
#             #     'response' :  recaptcha_response ,
#             # }
#             # r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
#             # # tji resulta
#             # result = r.json()
#             # if result['success']:
#                 user = form.save()
#                 username = form.cleaned_data.get('user')
#                 messages.success(request,'Created Successfully !')
#                 return redirect('authen')
#             # else:
#                 # messages.error(request, 'Invalid Recaptcha !') 
#     context = {'form':form}
#     return render(request , 'InscriptionEtudiant/formulaire.html', context)


# def userProfile(request):
#     context = {}
#     return render(request, 'InscriptionEtudiant/profile.html' , context)

















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
    form1=forms.StudentUserForm()
    form2=forms.StudentExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()
      
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            print('***************************************************')
            my_student_group[0].user_set.add(user)
            camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

            for i in range(10):
                return_value, image = camera.read()
                cv2.imwrite('.\\'+ str(i) + '.jpg', image)
            cv2.destroyAllWindows()
   
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


def save_capture(request):
    path = os.getcwd()
    file_name = "Attendance database"
    new_path = os.path.join(path, file_name)

    camera = cv2.VideoCapture(0)
    time.sleep(10)

    for i in range(10):
        return_value, image = camera.read()
        v = os.path.join(new_path, 'myImage001')
        cv2.imwrite(v + str(i) + '.jpg', image)
    del(camera)
        
        