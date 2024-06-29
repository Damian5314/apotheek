from django import forms
from .models import Profile, Collection, Medicine


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['BioText', 'City', 'DateOfBirth']
        widgets = {
            'DateOfBirth': forms.DateInput(attrs={'type': 'date'}),
        }


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['Medicine', 'User', 'Date']
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["Name", "Manufacturer", "Cures", "SideEffects"]
