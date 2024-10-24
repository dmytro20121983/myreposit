from dataclasses import fields
import email
from unicodedata import name
from django import forms
from django.forms import ModelForm
from .models import Bb, Piople

class BbForm (ModelForm):
    class Meta:
        model=Bb
        fields=('title', 'content', 'price', 'rubric')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
                 
        }

# Create Form Piople
class PiopleForm(ModelForm):
    
    class Meta:
        model = Piople
        fields = ('name', 'adress')
        
        widgets =  {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'adress': forms.TextInput(attrs={'class':'form-control'}),
            
        }
