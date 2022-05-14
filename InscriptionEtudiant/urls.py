from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
#from unicodedata import name 
#import cv2
#improt threading
#from InscriptionEtudiant.views import views
urlpatterns = [
    # path('accueil/',views.accueil) ,
    # path('inscri/',views.inscri , name='inscri'),
    # path('authen/',views.authen , name='authen'),
    # path('add_show',views.add_show, name='add_show'),
    # path('logout/',views.userLogout, name='logout'),
    # # path('updatestudent/',views.updatestudent, name='updatestudent'),
    # path('main/',views.main, name='main'),
    # path('delete/<int:id>/',views.delete_date, name='deletedata'),
    # path('<int:id>/',views.update_data, name ='updatedata'),
    # path('user/',views.userProfile, name='user_profile'),
    # path('nawal/', views.image_upload, name='image_upload'),
    # path('ikram/', views.testt, name='testt'),
    # path('forms/', views.forms, name='forms'),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('teacherclick', views.teacherclick_view),
    path('studentclick', views.studentclick_view),


    path('adminsignup', views.admin_signup_view),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('teachersignup', views.teacher_signup_view),
    path('adminlogin', LoginView.as_view(template_name='InscriptionEtudiant/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='InscriptionEtudiant/studentlogin.html')),
    path('teacherlogin', LoginView.as_view(template_name='InscriptionEtudiant/teacherlogin.html')),
    # path('capture', views.home_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='InscriptionEtudiant/index.html'),name='logout'),
    path('Attendance', views.take_attendance, name='take_attendance'),
    path('video', views.video_cap, name='video_cap'),
    path('capture', views.capture, name='capture'),

]
