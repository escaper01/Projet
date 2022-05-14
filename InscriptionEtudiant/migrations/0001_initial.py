# Generated by Django 3.0.5 on 2022-05-13 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=10, null=True)),
                ('date', models.DateField()),
                ('cl', models.CharField(max_length=10)),
                ('present_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=190)),
                ('confirm_password', models.CharField(max_length=190)),
                ('pays', models.CharField(max_length=70)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='InscriptionEtudiant/imagze')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('by', models.CharField(default='school', max_length=20, null=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.PositiveIntegerField()),
                ('joindate', models.DateField(auto_now_add=True)),
                ('mobile', models.CharField(max_length=40)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=13)),
                ('age', models.PositiveIntegerField()),
                ('matiere', models.CharField(choices=[('Sciences Mathémtiques et Informatique', 'Sciences Mathémtiques et Informatique'), ('Sciences Mathémtiques et Applications', 'Sciences Mathémtiques et Applications'), ('Sciences de la Matière Physique', 'Sciences de la Matière Physique'), ('Sciences de la Matière Chimie', 'Sciences de la Matière Chimie'), ('Sciences de la Vie', 'Sciences de la Vie'), ('Sciences de la Terre et de l univers', 'Sciences de la Terre et de l univers'), ('Cahiers des Normes Pédagogies Nationales', 'Cahiers des Normes Pédagogies Nationales')], max_length=40)),
                ('password', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
