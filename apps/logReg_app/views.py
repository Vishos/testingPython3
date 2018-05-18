from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(r):
    return render(r, 'logReg_app/index.html')

def processLogReg(r):
    result = ""
    if 'confirm' in r.POST:
        result = User.objects.validateRegistration(r.POST)
    else:
        result = User.objects.validateLogin(r.POST)
    if result['status']:
        r.session['user_id'] = result['user_id']
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(r, error)
    return redirect('/')


def success(r):
    return render(r, 'logReg_app/success.html')

def logout(r):
    r.session.clear()
    return redirect('/')
