
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('contact/',views.contact,name='contactpage'),
    path('course/',views.course,name='coursepage'),
    path('website/',views.website,name='websitepage'),
    path('pay/',views.pay,name='paypage'),
    path('code/',views.code,name='codepage'),
    path('interview/',views.interview,name='interviewquepage'),
    path('sub/',views.sub,name='subjectpage'),




    #course material
    path('cpp/',views.cpp,name='cpppage'),
    path('django/',views.django,name='djangopage'),



    #coding material
    path('ccode/',views.ccode,name='ccodepage'),
    
    
    
    #interview que
    path('pythonint/',views.pythonint,name='pythonintpage'),
    path('javaq/',views.javaq,name='javaintpage'),
    path('htmlq/',views.htmlq,name='htmlintpage'),
    path('javasq/',views.javasq,name='javasintpage'),
    path('cq/',views.cq,name='cintpage'),
    path('djangoq/',views.djangoq,name='djangointpage'),
    path('cppq/',views.cppq,name='cppintpage'),
    path('csq/',views.csq,name='csintpage'),
    


]