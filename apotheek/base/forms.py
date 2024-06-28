from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['BioText', 'City', 'DateOfBirth']
        widgets = {
            'DateOfBirth': forms.DateInput(attrs={'type': 'date'}),
        }
