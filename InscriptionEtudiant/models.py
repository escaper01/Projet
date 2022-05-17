#from distutils.command.upload import upload
from asyncio.windows_events import NULL
import email
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Image(models.Model):
    username = models.CharField(max_length=30)
    image = models.ImageField(upload_to='InscriptionEtudiant/imagze')




classes=[('Sciences Mathémtiques et Informatique','Sciences Mathémtiques et Informatique'),('Sciences Mathémtiques et Applications','Sciences Mathémtiques et Applications'),('Sciences de la Matière Physique','Sciences de la Matière Physique'),
('Sciences de la Matière Chimie','Sciences de la Matière Chimie'),('Sciences de la Vie','Sciences de la Vie'),('Sciences de la Terre et de l univers','Sciences de la Terre et de l univers'),('Cahiers des Normes Pédagogies Nationales','Cahiers des Normes Pédagogies Nationales')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE , unique=True)
    mobile=models.CharField(max_length=13)
    age=models.PositiveIntegerField(null=True)
    matiere=models.CharField(max_length=40,choices=classes)
    image = models.FilePathField(path='C:\\Users\\escaper\\OneDrive\\Bureau\\projects\\face detection\\Projet\\InscriptionEtudiant\\Attendance database',recursive=True, null=True, blank=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User) #signal used to create a object related to user instance
def create_user_student(sender, instance, created, **kwargs):
    if created:
        StudentExtra.objects.create(user=instance)

@receiver(post_save, sender=User) #signal used to save a object related to user instance
def save_user_student(sender, instance, **kwargs):
    instance.studentextra.save()