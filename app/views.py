# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField
from app.models import Paymenttype, Programme, Departments, Intakes, Cons, Students, student_status, Reciept
from re import template
from django.db.models import Q
from django.views.generic import ListView
import os
from uuid import uuid4
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter
from django.contrib.staticfiles import finders
# from app.EmailBackEnd import EmailBackEnd




def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('adminpage')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'hod_template/add_staff_template.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('adminpage')
            # elif user is not None and user.is_customer:
            #     login(request, user)
            #     return redirect('customer')
            # elif user is not None and user.is_employee:
            #     login(request, user)
            #     return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'hod_template/home_content.html')


# def home(request):
#     return render(request, 'index.html')


# def loginPage(request):
#     return render(request, 'login.html')



# def doLogin(request):
#     if request.method != "POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
#         if user != None:
#             login(request, user)
#             user_type = user.user_type
#             #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
#             if user_type == '1':
#                 return redirect('admin_home')
                
#             elif user_type == '2':
#                 # return HttpResponse("Staff Login")
#                 return redirect('staff_home')
                
#             elif user_type == '3':
#                 # return HttpResponse("Student Login")
#                 return redirect('finance_home')

#             else:
#                 messages.error(request, "Invalid Login!")
#                 return redirect('login')
#         else:
#             messages.error(request, "Invalid Login Credentials!")
#             #return HttpResponseRedirect("/")
#             return redirect('login')



# def get_user_details(request):
#     if request.user != None:
#         return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
#     else:
#         return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

