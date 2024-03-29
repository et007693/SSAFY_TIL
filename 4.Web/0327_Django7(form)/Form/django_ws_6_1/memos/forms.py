from django import forms
from .models import Memo

class Memoform(forms.ModelForm):
    class Meta:
        model = Memo
        fields = '__all__'
        