from django import forms
from crudapp.models import User # form jaita banabo model er upor base koray banabo tai eta import kora

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        widgets = {
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'uemail':forms.TextInput(attrs={'class':'form-control'}),
            'upassword':forms.TextInput(attrs={'class':'form-control'})
        }