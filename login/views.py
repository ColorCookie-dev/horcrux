from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm



# Create your views here.
def indexView(request):
    return render(request,'index')
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request): 
	if request.user.is_authenticated:
		return redirect('index.html')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')


		context = {'form':form}
		return render(request, 'login/register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("index.html")
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user =authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index.html')
            else:
                messages.info(request,'Username OR password is not matched')
    context ={}
    return render(request,'login/login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')
