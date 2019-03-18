from .models import WikiEntryModel, RIEntryModel
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username",
                  "email",
                  "password",
                  ]
        # fields = "__all__"

class WikiEntryForm(forms.ModelForm):
    class Meta:
        model = WikiEntryModel
        exclude = ["creator"]


class RIEntryForm(forms.ModelForm):
    class Meta:
        model = RIEntryModel
        exclude = ["wiki", "createdDate"]
