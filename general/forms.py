from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            "first_name",
            "last_name",
            "email"
        ]

        widgets = {

            "first_name": forms.TextInput(

                attrs={
                    "placeholder": "Enter your first name",
                    "class": "form-control"
                }

            ),

            "last_name": forms.TextInput(

                attrs={
                    "placeholder": "Enter your last name",
                    "class": "form-control"
                }

            ),

            "email": forms.EmailInput(

                attrs={
                    "placeholder": "Enter your email address",
                    "class": "form-control"
                }

            ),

        }