from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from doctor.models import (Doctor,Patient, Make_appointment, Validate_appointment, Recharge_balance, CreateReport,
                           CreateDrReport, CreatePrescription)

class DoctorSignUpForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('username', 'email', 'gender', 'year', 'month', 'date', 'specialities', 'education'
        ,'hospitals', 'rate', 'description' ,'port')


class PatientSignUpForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('username', 'email', 'gender', 'year', 'month', 'date', 'age', 'port')



class Make_appointment_form(forms.ModelForm):
    class Meta:
        model = Make_appointment
        fields = ('doctorEmailId', 'year', 'month', 'date', 'hr', 'min', 'problems')






class Recharge_form(forms.ModelForm):
    class Meta:
        model = Recharge_balance
        fields = '__all__'


class CreateReport_form(forms.ModelForm):
    class Meta:
        model = CreateReport
        fields = '__all__'


class Validate_appointment_form(forms.ModelForm):
    class Meta:
        model = Validate_appointment
        fields = ('appointment_id', 'year', 'month', 'date', 'hr','min', 'changedatetime')


class CreateDrReport_form(forms.ModelForm):
    class Meta:
        model = CreateDrReport
        fields = '__all__'



class Prescription_form(forms.ModelForm):
    class Meta:
        model = CreatePrescription
        fields = '__all__'







# class Custom_doctor_form(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Custom_doctor
#         fields = ('username', 'email', 'password', 'phone_no', 'gender', 'year', 'month', 'date', 'specialities', 'education'
#                   , 'hospitals', 'rate')

#
# class Custom_patient_form(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Custom_patient
#         fields = ('username', 'email', 'password', 'gender', 'year', 'month', 'date', 'age')
#
#
#
#
#
#
