from django.shortcuts import render
from django.http import HttpRequest
from .forms import StudentRegistration 
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, 'blog/home.html')
def about(request):
    return render(request, 'blog/about.html')  
def contact(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Your Data Has Been Submited........')
    else:
        fm = StudentRegistration()
    return render(request, 'blog/contact.html' , {'form':fm})

def website(request): 
    return render(request, 'blog/website.html')

def pay(request):
    return render(request, 'blog/pay.html')

def interview(request):
    return render(request, 'blog/interview.html')
def code(request):
    return render(request, 'blog/code.html')
def sub(request):
    return render(request, 'blog/sub.html')



















def course(request):
    return render(request, 'blog/course.html')



#coures
def cpp(request):
    return render(request, 'blog/program/cpp.html')
def django(request):
    return render(request, 'blog/program/django.html')




def ccode(request):
    return render(request, 'blog/program/ccode.html')















# interview que
def javaq(request):
    return render(request, 'blog/program/javaque.html')
def pythonint(request):
    return render(request, 'blog/program/pythonque.html')
def htmlq(request):
    return render(request, 'blog/program/htmlque.html')
def javasq(request):
    return render(request, 'blog/program/javasque.html')
def cq(request):
    return render(request, 'blog/program/cque.html')
def djangoq(request):
    return render(request, 'blog/program/djangoque.html')
def cppq(request):
    return render(request, 'blog/program/cppque.html')
def csq(request):
    return render(request, 'blog/program/csq.html')
