from django.http import HttpResponse , StreamingHttpResponse ,  HttpResponseRedirect, JsonResponse 
from django.contrib.auth import authenticate , login , logout
from .decorators import allowedUsers , forAdmins
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.files import File
from .models import StudentExtra
from cv.agent import VideoCamera
from .models import *
from .forms import *
import os
import time

############################################TEST########################
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'InscriptionEtudiant/accueil.html')



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
    form1 = AdminSigupForm()
    form2 = StudentUserForm()
    all_forms = {
        'form1': form1,
        'form2': form2,
    }

    if request.POST:
        v_form1 = AdminSigupForm(request.POST)
        if v_form1.is_valid():
            current_user = v_form1.save()

        # print(request.POST)
        current_student = StudentExtra.objects.get(id=current_user.id)

        current_student.mobile = request.POST.get('mobile')
        current_student.age = request.POST.get('age')
        current_student.matiere = request.POST.get('matiere')
        current_student.save()
        
            
        return HttpResponseRedirect('studentlogin')
    return render(request,'InscriptionEtudiant/studentsignup.html',context={'form': all_forms})


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






# #for checking user is techer , student or admin
# def is_admin(user):
#     return user.groups.filter(name='ADMIN').exists()
# def is_teacher(user):
#     return user.groups.filter(name='TEACHER').exists()
# def is_student(user):
#     return user.groups.filter(name='STUDENT').exists()


# def afterlogin_view(request):
#     if is_admin(request.user):
#         return redirect('admin-dashboard')
#     elif is_teacher(request.user):
#         accountapproval=models.TeacherExtra.objects.all().filter(user_id=request.user.id,status=True)
#         if accountapproval:
#             return redirect('teacher-dashboard')
#         else:
#             return render(request,'InscriptionEtudiant/teacher_wait_for_approval.html')
#     elif is_student(request.user):
#         accountapproval=models.StudentExtra.objects.all().filter(user_id=request.user.id,status=True)
#         if accountapproval:
#             return redirect('student-dashboard')
#         else:
#             return render(request,'InscriptionEtudiant/student_wait_for_approval.html')



def sign_in_gen(camera, username):
    start = time.time()
    while True:
        sec_diff = int(time.time() - start)
        if sec_diff == 4:
            camera.shoot(username)
            break
        frame = camera.cam_stream()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_cap(request):
    cam = VideoCamera()
    username = request.COOKIES.get('username') 
    return StreamingHttpResponse(sign_in_gen(camera=cam,username= username),content_type='multipart/x-mixed-replace; boundary=frame')

        

# def capture(request):
#     username = request.POST.get('name')
#     shoot = request.POST.get('shoot')
#     data = dict()
#     if username and shoot:
#         data['username'] = username
#         data['shoot'] = True
    
#     return JsonResponse(data)


