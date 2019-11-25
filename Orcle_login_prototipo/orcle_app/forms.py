from django import forms

class login_form(forms.Form):
    email= forms.EmailField()
    senha= forms.CharField()

  
    
    