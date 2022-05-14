#from distutils.command.upload import upload
from asyncio.windows_events import NULL
import email
from django.db import models
from django.contrib.auth.models import User

# class Etudiant(models.Model):
#     nom = models.CharField(max_length=20 , blank=False)
#     prenom = models.CharField(max_length=20 , blank=False)
#     email = models.EmailField(max_length=100 , blank=False)
#     phone = models.IntegerField(blank=False)
#     age = models.IntegerField(blank=False)
#     password= models.CharField(max_length=190 , blank=False)
#     confirm_password= models.CharField(max_length=190 , blank=False)
#     pays = models.CharField(max_length=70 , blank=False)
#     date_created = models.DateTimeField(auto_now_add=True ,blank=True)
#     #speciality = models.CharField(max_length=190,blank=False,choices=STATUS)
#     def __str__(self):
#         return self.nom
        

class Image(models.Model):
    username = models.CharField(max_length=30)
    image = models.ImageField(upload_to='InscriptionEtudiant/imagze')





class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('Sciences Mathémtiques et Informatique','Sciences Mathémtiques et Informatique'),('Sciences Mathémtiques et Applications','Sciences Mathémtiques et Applications'),('Sciences de la Matière Physique','Sciences de la Matière Physique'),
('Sciences de la Matière Chimie','Sciences de la Matière Chimie'),('Sciences de la Vie','Sciences de la Vie'),('Sciences de la Terre et de l univers','Sciences de la Terre et de l univers'),('Cahiers des Normes Pédagogies Nationales','Cahiers des Normes Pédagogies Nationales')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE , unique=True)
    first_name=models.CharField(max_length=40,null=False)
    last_name=models.CharField(max_length=40,null=False)
    email=models.EmailField(max_length=100 , blank=False)
    mobile=models.CharField(max_length=13)
    age=models.PositiveIntegerField(null=False)
    matiere=models.CharField(max_length=40,choices=classes)
    password=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    image = models.FilePathField(path='C:\\Users\\escaper\\OneDrive\\Bureau\\projects\\face detection\\Projet\\InscriptionEtudiant\\Attendance database',recursive=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)