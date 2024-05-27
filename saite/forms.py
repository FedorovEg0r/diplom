from django import forms
from .models import City
from telegram_auth.models import ParserSetting

class ParserForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="Город")

    class Meta:
        model = ParserSetting
        fields = ['city', 'keywords']
        widgets = {
            'keywords': forms.HiddenInput(attrs={'id': 'id_keywords'}),
        }