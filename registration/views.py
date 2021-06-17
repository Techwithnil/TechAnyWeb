from .import forms
from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import SineUpForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
# Create your views here.
def profile(request):
    if request.method=='POST':
       u_form = UserUpdateForm(
           request.POST,
           instance=request.user
       )
       p_form = ProfileUpdateForm(
           request.POST,request.FILES,
           instance=request.user.profile
       )

       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request,f'Your account has been updated')
           return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form' : u_form,
            'p_form' : p_form
        }

    return render(request, 'registration/profile.html',context)

def register(request):
    if request.method == "POST":
        fm = SineUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SineUpForm()
    return render(request, 'registration/register.html', {'form': fm})