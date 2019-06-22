from django.db import models
gender_choice = [('MALE', 'male'), ('female', 'FEMALE')]


class Doctor(models.Model):
    username = models.CharField(max_length=500)
    gender = models.CharField(max_length=50)
    year = models.IntegerField()
    month = models.CharField(max_length=50)
    date = models.CharField(max_length= 50)
    specialities = models.CharField(max_length=1000)
    education = models.CharField(max_length=1000)
    hospitals = models.CharField(max_length=1000, null =True)
    rate = models.FloatField()
    email = models.EmailField(unique=True)
    description = models.TextField()
    port = models.IntegerField()


class Patient(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    year = models.IntegerField()
    month = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    port = models.IntegerField()


class Make_appointment(models.Model):
    doctorEmailId = models.EmailField()
    year = models.IntegerField()
    month = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    hr = models.IntegerField()
    min = models.IntegerField()
    problems = models.CharField(max_length=9000)


class Recharge_balance(models.Model):
    recharge_card = models.IntegerField(default=0)


class CreateReport(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    institute = models.CharField(max_length=1000)



class Validate_appointment(models.Model):
    appointment_id = models.IntegerField()
    year = models.IntegerField()
    month = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    hr = models.IntegerField()
    min = models.IntegerField()
    changedatetime = models.BooleanField(default=False)

class CreateDrReport(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    institute = models.CharField(max_length=1000)
    patient = models.EmailField(max_length=500)


class CreatePrescription(models.Model):
    diagnosis = models.CharField(max_length=20000)
    medications = models.CharField(max_length=10000)
    patient = models.EmailField(max_length=100)







































# # Create your models here.
# class Custom_doctor(AbstractUser):
#     gender = models.CharField(max_length=50)
#     year = models.IntegerField()
#     month = models.CharField(max_length=50)
#     date = models.CharField(max_length= 50)
#     specialities = models.CharField(max_length=1000)
#     education = models.CharField(max_length=1000)
#     hospitals = models.CharField(max_length=1000)
#     rate = models.FloatField()
#     email = models.EmailField(unique=True)
#     phone_no = models.CharField(max_length=20)
#
#
