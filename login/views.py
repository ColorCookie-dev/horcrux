from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm
from .models import User, Organisation as Org


def logged_out_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return view_func(request, *args, **kwargs)
    return wrapper

def get_comp_name():
    return User.objects.get(is_superuser=True).org.name

def get_def_context(request):
    return {
            'companyname': get_comp_name(),
            }

# Create your views here.
@login_required(login_url='/login/')
def indexView(request):
    context = get_def_context(request)
    if request.user.has_perm('login.view_user'):
        if not request.user.is_superuser:
            user_org = request.user.org
            context['members'] = User.objects.filter(org=user_org)
        else:
            context['members'] = User.objects.all()

    return render(request, 'index.html', context)

@logged_out_required
def registerView(request): 
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login/')

    form = CreateUserForm()
    context = get_def_context(request)
    context['form'] = form
    return render(request, 'login/register.html', context)

@logged_out_required
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is not matched')
    context = get_def_context(request)
    return render(request, 'login/login.html', context)

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login/')
