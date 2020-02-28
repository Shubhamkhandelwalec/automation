from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from . import emailsmtp
from random import randint
import datetime
import base64
import hashlib
def Register(request):
    if request.method == 'POST':
        try:
            form1 = Signup(request.POST,request.FILES)
            if form1.is_valid():
                try:

                    username = request.POST.get('username')
                    fullname = request.POST.get('fullname')
                    emails = request.POST.get('email')
                    print(username,fullname,emails)
                    randomnumber = randint(10**(9-1),(10**9)-1)
                    currenttime = datetime.datetime.now()
                    print(randomnumber)
                    url = emailsmtp.Sendingemail((fullname, username, emails, randomnumber, currenttime))

                    emailobj = emailsmtp.Emailsend(emails,url,username)
                    obj1=Registration(user_name=username,full_name=fullname,email=emails,randomid=int(randomnumber))
                    obj1.save()
                    return render(request,'sent.html',{"message":"Email successfully sent...Please check your mail"})
                except :
                    return render(request,'sent.html',{"message":"Unable to send mail..Please try again"})

            else:
                return render(request, 'register.html', {"form": form1})

        except Exception as e:
            print(e)
            return render(request, 'register.html', {"data": "500,Internal server error"})
    else:
        form1 = Signup()
    return render(request,'register.html',{"form":form1})

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            passcode = request.POST.get('password')
            print("---->",username,passcode)
            var = Registration.objects.filter(user_name=username,password=hashlib.sha224(passcode.encode()).hexdigest()).exists()
            print(var)
            if var:
                return redirect("/users/dashboard/")
            else:
                return render(request, "login.html", {"form":form,"data": "Login authentication not valid"})
        else:
            return render(request, 'login.html',{"form":form})
    else:
        form = LoginForms()
    return render(request,'login.html',{"form":form})

def dash(request):
    var = Registration.objects.all()
    return render(request,'dashboard.html',{"data":var})

def edit(request,update):
    detail = Registration.objects.get(id=update)
    if request.method == 'POST':
        form = Updatedform(request.POST)
        if form.is_valid():
            if hashlib.sha224(request.POST.get('password').encode()).hexdigest() == detail.password:
                if request.POST.get('username') != "" and request.POST.get('username') != " " and request.POST.get('username') != None:
                    detail.user_name = request.POST.get('username')
                    detail.save()
                if request.POST.get('full_name') != "" and request.POST.get('full_name') != " " and request.POST.get('full_name') != None:
                    detail.full_name = request.POST.get('full_name')
                    detail.save()
                if request.POST.get('email') != "" and request.POST.get('email') != " " and request.POST.get('email') != None:
                    detail.email = request.POST.get('email')
                    detail.save()
                if request.FILES:
                    if request.FILES['pics'] != "" and request.FILES['pics'] != " " and request.FILES['pics'] != None:
                        print(request.FILES['pics'])
                        detail.profile_img = request.FILES['pics']
                        detail.save()
                else:
                    return redirect("/users/dashboard/")
                return redirect("/users/dashboard/")
            else:
                return render(request, 'edit.html', {"detail": detail, "error": "password does not match"})
        else:
            return render(request, 'edit.html', {"detail": detail, "form": form})
    else:
        form = Updatedform()
    return render(request,'edit.html',{"detail":detail,"form":form})
def delete(request,delid):
    try:
        detail = Registration.objects.get(id=delid)
        if detail.id:
            detail.delete()
            return redirect("/users/dashboard/")
    except:
        return render(request, 'dashboard.html', {"error": "Data doesn't exist"})
# def realregistration(request):
#
#     return render(request, 'verify.html')
def get(request):
    try:
        decoded = eval(base64.b64decode(request.GET['key']).decode())
        print("decoded is ",decoded)
        if request.method == 'POST':
            if Registration.objects.filter(full_name=decoded[0], user_name=decoded[1], email=decoded[2],
                                           randomid=decoded[3]).exists():

                form = Verification(request.POST)
                if form.is_valid():
                    passcode = request.POST.get('password')
                    confirm_passcode = request.POST.get('confirm_password')
                    print(passcode, confirm_passcode, decoded[3])
                    tempdata = Registration.objects.get(randomid=decoded[3])
                    tempdata.password = hashlib.sha224(passcode.encode()).hexdigest()
                    tempdata.isverified = True
                    tempdata.save()
                    return redirect("/users/dashboard/")
                else:
                    return render(request, 'verify.html', {"form": form})
        if Registration.objects.filter(full_name=decoded[0],user_name=decoded[1],email=decoded[2],randomid=decoded[3]).exists():

            return render(request,'verify.html')
        else:
            return render(request,'sent.html',{"message":"You are not authorised user"})

    except Exception as e :
        return render(request,'verify.html',{"error":e})

def view_404(request,exception):
    return render(request,'index.html')