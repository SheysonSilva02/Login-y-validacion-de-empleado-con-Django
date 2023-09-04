from django import forms 
from .models import registros

class registrosform(forms.ModelForm):
    
    class Meta:
        model = registros
        fields = '__all__'
    
