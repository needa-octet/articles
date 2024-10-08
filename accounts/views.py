from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def login_view(request):
    # print("tHIS IS CREDENTIALS",request.POST)
   
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        # user = authenticate(request,username=username,password=password)
        # if user is None:
        #     context={
        #         "error":"Invalid username or password.",
        #     }
        #     return render(request,"accounts/login.html",context=context)
        # login(request,user)
        if(form.is_valid()):
            user=form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm(request)
    context={
        "form":form
    }
    return render(request,"accounts/login.html",context)
        

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('/login/')
    return render(request,"accounts/logout.html",context={})

def register_view(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context={"form":form}
    return render(request,"accounts/register.html",context=context)
# In views.py of one of your apps
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_superuser_view(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'needa@octet.com', 'Needa#710')
        return HttpResponse('Superuser created.')
    return HttpResponse('Superuser already exists.')