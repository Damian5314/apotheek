from django import forms
from .models import Profile, Medicine


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['BioText', 'City', 'DateOfBirth']
        widgets = {
            'DateOfBirth': forms.DateInput(attrs={'type': 'date'}),
        }

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["Name", "Manufacturer", "Cures", "SideEffects"]
