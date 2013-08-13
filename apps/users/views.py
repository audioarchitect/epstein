from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from apps.bands.models import Band, UserHasBand
from apps.events.models import Event 

from apps.home.views import LoginForm

def index(request):
    my_data = {}
    return render_to_response( 'users/index.html', my_data, context_instance=RequestContext(request) )

def do_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']   
        else:
            email =''
            password = ''

    user = authenticate( username=email, password=password )
  
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

# try to login the user
def doo_login(request):
    email    = request.POST.get( 'login_email', '' )
    password = request.POST.get( 'login_password', '' )   
    user = authenticate( username=email, password=password )
  
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        
# try to logout the user
def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def new(request):
    my_data = {}
    return render_to_response( 'users/new.html', my_data, context_instance=RequestContext(request) )

def create(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name    = form.cleaned_data['name']
            email   = form.cleaned_data['email']
            password = form.cleaned_data['password'] 
            password2 = form.cleaned_data['password2']  
        else:
            email =''
            password = ''
    #name = request.POST.get( 'name', '' )
    #email = request.POST.get( 'email', '' )
    #password = request.POST.get( 'password', '' )
    #password_confirm = request.POST.get( 'password_confirm', '' )
    user = User.objects.create_user( email, email, password )
    user.first_name = name
    user.save()
    
    user_login = authenticate( username=email, password=password )
    if user_login is not None:
        login(request,user_login)
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/')
    
def dashboard(request):
    userid = request.user.id
    pookies = UserHasBand.objects.filter(user_id = userid)
    bands = []
    band_ids = []

    for pook in pookies:
        band = Band.objects.get(pk=pook.band_id) 
        bands.append( band )
        band_ids.append( band.id )

    events = Event.objects.filter(band_id__in=band_ids).order_by('date')[:4]
    news = [ { 'user' : 'John', 'msg' : "Placeholder text..." }, {'user' : 'Bob', 'msg' : "I will implement this soon!!!" } ]
    view_data = { "bands" : bands, "news" : news, "events" : events }
    return render_to_response( 'users/dashboard.html', view_data, context_instance=RequestContext(request) )