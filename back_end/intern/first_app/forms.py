from django import forms
from django.forms import Textarea
from django.contrib.auth.models import User
from first_app.models import Post,FormSl


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    number = forms.IntegerField()
    text = forms.CharField(widget = forms.Textarea)
class FormN(forms.Form):
    
    class Meta:
        model = Post
        fields = ('name','email','number','comments')
        widgets = {'comments' : Textarea(attrs = {'rows': 7, 'cols': 40})}
class SignupForm(forms.ModelForm):
    class Meta:
        model = FormSl
        fields = '__all__'
        widgets = {
            'up' : forms.PasswordInput(),
            'up2' : forms.PasswordInput()
        }

class LoginForm(forms.Form):
    class Meta:
        model = LoginMod
        fields = '__all__'
        widgets = {
            'password' : forms.PasswordInput()
        }
    
        
      