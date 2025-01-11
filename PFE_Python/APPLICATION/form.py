from django import forms
from django.contrib.auth.forms import UserCreationForm

class Forminscription(UserCreationForm):
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
           
           
        }),
    )
    password2 = forms.CharField(
        label="Mot de passe confirmation",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
           
            
        }),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={
                
                
            }),
        }
