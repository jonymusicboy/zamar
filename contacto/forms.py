from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'telefono', 'asunto', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            'asunto': forms.TextInput(attrs={'placeholder': 'Asunto'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mensaje'}),
        }
