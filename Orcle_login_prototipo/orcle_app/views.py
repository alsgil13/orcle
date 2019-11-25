import os
from django.shortcuts import render
from . import forms

# Create your views here.
os.system('cls')

def index(request):
    my_dict= {'content':"testando!"}
    return render(request,'orcle_app/index.html',context= my_dict)

def login(request):
    form= forms.login_form()#1 
    

    if request.method == "POST":
        form= forms.login_form(request.POST)
        
        if form.is_valid():
            print("testando!#############################")
            print(form.cleaned_data['email'])
            print(form.cleaned_data['senha'])

    return render(request,'orcle_app/login.html',{'v_form':form})#2