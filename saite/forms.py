from django import forms
from .models import Parser, City

class ParserForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="Город")

    class Meta:
        model = Parser
        fields = ['city', 'keywords']
        widgets = {
            'keywords': forms.HiddenInput(attrs={'id': 'id_keywords'}),
        }
