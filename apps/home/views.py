from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django import forms

class LoginForm(forms.Form):
    email 		= forms.EmailField( widget=forms.TextInput( attrs={'placeholder': 'Email Address'} ) )
    password 	= forms.CharField( widget=forms.PasswordInput( attrs={'placeholder': 'Password'} ) )

class RegisterForm(forms.Form):
    name		= forms.CharField( widget=forms.TextInput( attrs={ 'placeholder': 'Name'} ))
    email 		= forms.EmailField( widget=forms.TextInput( attrs={'placeholder': 'Email Address'} ) )
    password 	= forms.CharField( widget=forms.PasswordInput( attrs={'placeholder': 'Password'} ) )
    password2 	= forms.CharField( widget=forms.PasswordInput( attrs={'placeholder': 'Confirm password'} ) )

def index(request):
    login_form 		= LoginForm(request.POST)
    register_form 	= RegisterForm(request.POST)

    view_data = { 'user': request.user, 'login_form' : login_form, 'register_form' : register_form }
    if request.user.is_authenticated():
    	return HttpResponseRedirect('/dashboard/')
    else:
        return render_to_response( 'home.html', view_data, context_instance=RequestContext(request) )

def about(request):
    return render_to_response( 'about.html', context_instance=RequestContext(request) )

def contact(request):
    return render_to_response( 'contact.html', context_instance=RequestContext(request) )