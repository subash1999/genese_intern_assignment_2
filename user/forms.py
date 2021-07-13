from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import UserProfile
from django.forms import ModelForm
import re


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].help_text = ""

    class Meta:
        model = User
        fields = ("username","email", "password1", "password2")
    
    # def clean_password2(self,*args, **kwargs):
    #     super(CustomUserCreationForm,self).clean_password2(*args, **kwargs)
    #     password = self.cleaned_data['password2']
    #     Flag = True

    #     if password.islower():
    #         Flag = False
    #     elif '@' not in password and '-' not in password and '|' not in password:
    #         Flag = False
    #     elif not re.search("[a-z]", password) and not  re.search("[A-Z]", password):
    #         Flag = False
            
    #     if not Flag:
    #         raise forms.ValidationError("Password must have atleast one alphabet, special character and upper case character.")

        # return password

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserProfileForm(ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['dob','phone','address','image']

        
class UserUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        
    class Meta:
        model = User
        fields = ['email','first_name','last_name']

