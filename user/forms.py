from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        help = self.fields['password1'].help_text
        help = help.split("</ul>")[0]+"<li>Your password must contain atleast 1 uppercase character.</li></ul>"
        self.fields['password1'].help_text = help

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def clean_password1(self):
        password = self.cleaned_data['password1']
        if password.islower():
            raise forms.ValidationError("Password must contain atleast one upper case character.")
        return password

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user