from .models import WikiEntryModel, RIEntryModel
from django import forms
from django.contrib.auth.models import User


#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["username",
#                   "email",
#                   "password",
#                   ]
#
#     def clean_username(self):
#         username= self.cleaned_data.get("username")
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("Username is taken")
#         return username

class NewUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Username"
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email"
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"
        }))
    password2 = forms.CharField(label="confirmPassword", widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Confirm Password"
        }))

    def clean_username(self):
        username = self.cleaned_data["username"]
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username


class WikiEntryForm(forms.ModelForm):
    class Meta:
        model = WikiEntryModel
        exclude = ["creator"]


class RIEntryForm(forms.ModelForm):
    class Meta:
        model = RIEntryModel
        exclude = ["wiki", "createdDate"]
