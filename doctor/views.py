from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView
from doctor.models import Patient, Doctor, Make_appointment, Validate_appointment, Recharge_balance, CreateReport, CreateDrReport
from doctor.forms import PatientSignUpForm, DoctorSignUpForm, Validate_appointment_form, Recharge_form, Prescription_form, Make_appointment_form, CreateDrReport_form, CreateReport_form
from django.contrib.auth.decorators import login_required
import requests
import json




from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')


def doctor(request):
    return render(request, 'doctor.html')

def patient(request):
    return render(request, 'patient.html')


def doctor_signup(request):
    if request.method == 'GET':
        custom_doctor_form = DoctorSignUpForm()
        return render(request, 'doctor_signup.html', {'form':custom_doctor_form})
    else:
        doc_dict = {
            "$class": "com.pax.drsewa.CreateDoctor",
            "emailId": "string",
            "name": "string",
            "year": 0,
            "month": 0,
            "date": 0,
            "gender": "MALE",
            "specialities": [],
            "education": [],
            "description": "string",
            "hospitals": [],
            "rate": 0
        }

        user = Doctor(request.POST)
        doc_dict['name'] = request.POST['username']
        doc_dict['emailId'] = request.POST['email']
        doc_dict['year'] = request.POST['year']
        doc_dict['month'] = request.POST['month']
        doc_dict['date'] = request.POST['date']
        doc_dict['gender'] = request.POST['gender']
        specialities = request.POST['specialities']
        specialities = specialities.split(",")
        specialities_list = [i.lstrip() for i in specialities]
        doc_dict['specialities'] = specialities_list
        education = request.POST['education']
        education = education.split(',')
        education_list = [i.lstrip() for i in education]
        doc_dict['education'] = education_list
        doc_dict['description'] = request.POST['description']
        hospitals = request.POST['hospitals']
        hospitals = hospitals.split(',')
        hospitals_list = [i.lstrip() for i in hospitals]
        doc_dict['hospitals'] = hospitals_list
        doc_dict['rate'] = request.POST['rate']

        doc_dict_json = json.dumps(doc_dict)

        output = requests.post('http://localhost:3000/api/CreateDoctor', headers={"content-type": "application/json"}   , data=doc_dict_json)
        if (output.status_code == 200):
            return HttpResponse(output.text+"<br><br><br>"+doc_dict_json)
        else:
            print(output.json)
            return HttpResponse('Something Error: <br>'+ output.text+"<br><br><br>"+doc_dict_json+"<br><br><br>"+"json: "+ str(output.status_code))

def doctor_login(request):
    if request.method == 'GET':
        custom_doctor_form = DoctorSignUpForm()
        return render(request, 'doctor_login.html', {'form':custom_doctor_form})

    else:

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate(username=username, password=password, email=email)


        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('doctor_login')
            else:
                messages.warning(request, 'Sorry, You are not active.')
                return redirect('doctor_signup')

        else:
            messages.error(request, 'Sorry Recheck your username or password')
            return redirect('doctor_signup')


def doctor_logout(request):
    logout(request)
    return redirect("doctor_login")


def patient_signup(request):
    if request.method == 'GET':
        custom_patient_form = PatientSignUpForm()
        return render(request, 'doctor_signup.html', {'form':custom_patient_form})
    else:
        patient_dict = {
                "$class": "com.pax.drsewa.CreatePatient",
                "emailId": "string",
                "name": "string",
                "year": 0,
                "month": 0,
                "date": 0,
                "gender": "MALE"
        }

        user = Patient(request.POST, request.FILES)
        patient_dict['name'] = request.POST['username']
        patient_dict['emailId'] = request.POST['email']
        patient_dict['year'] = request.POST['year']
        patient_dict['month'] = request.POST['month']
        patient_dict['date'] = request.POST['date']
        patient_dict['gender'] = request.POST['gender']

        patient_dict_json = json.dumps(patient_dict)

        output = requests.post('http://localhost:3000/api/CreatePatient', headers={"content-type": "application/json"}, data=patient_dict_json)
        if (output.status_code == 200):
            return HttpResponse(output.text + "<br><br><br>" + patient_dict_json)
        else:
            print(output.json)
            return HttpResponse(
                'Something Error: <br>' + output.text + "<br><br><br>" + patient_dict_json + "<br><br><br>" + "json: " + str(
                    output.status_code))


def patient_login(request):
    if request.method == 'GET':
        custom_patient_form = PatientSignUpForm()
        return render(request, 'patient_login.html', {'form':custom_patient_form})

    else:

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        port = request.POST.get('port')

        #user = authenticate(username=username, password=password, email=email)

        output = requests.get('http://localhost:3000/api/Doctor', headers={"content-type": "application/json"}, data=patient_dict_json)

        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('patient_login')
            else:
                messages.warning(request, 'Sorry, You are not active.')
                return redirect('patient_signup')

        else:
            messages.error(request, 'Sorry Recheck your username or password')
            return redirect('patient_signup')


def patient_logout(request):
    logout(request)
    return redirect("patient_login")



@login_required(login_url='index.html')
def makeappointment(request):
    if request.method == 'GET':
        appointment = Make_appointment_form()
        return render(request, 'makeappointment.html', {'form':appointment})

    else:
        appointment_form = Make_appointment_form(request.POST)
        if appointment_form.is_valid():

            return HttpResponse('Submitted')
        else:
            return HttpResponse('Not Submitted')


def doctors(request):
    doctors = Doctor.username
    return render(request, 'doctors.html', context={'doctors': doctors})

def validate(request):
    validate = Validate_appointment_form()
    pass

def createreport(request):
    if request.method == 'GET':
        report = CreateReport_form()
        return render(request, 'createreport.html', {'form':report})

    else:
        report_form = CreateReport_form(request.POST)
        if report_form.is_valid():
            return HttpResponse('Submitted')
        else:
            return HttpResponse('Not Submitted')

def drreport(request):
    if request.method == 'GET':
        report = CreateDrReport_form()
        return render(request, 'drreport.html', {'form':report})

    else:
        report_form = CreateDrReport_form(request.POST)
        if report_form.is_valid():
            return HttpResponse('Submitted')
        else:
            return HttpResponse('Not Submitted')


def recharge(request):
    if request.method == 'GET':
        card = Recharge_form()
        return render(request, 'recharge.html', {'form':card})

    else:
        card = Recharge_form(request.POST)
        if card.is_valid():
            card.recharge_card+=card
            return HttpResponse('Balance added successfully')

        else:
            return HttpResponse('Please enter valid amount')


def prescription(request):
    if request.method == 'GET':
        prescription = Prescription_form()
        return render(request, 'prescription.html', {'form': prescription})

    else:
        prescription = Prescription_form(request.POST)
        if prescription.is_valid():
            prescription.save()
            return HttpResponse('Saved successfully!')