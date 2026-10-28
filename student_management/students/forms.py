from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'course']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number'
            }),
            'course': forms.TextInput(attrs={
                'placeholder': 'Enter your course'
            }),
        }