from django import forms
from .models import Restaurant, Menu


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'descriptions':forms.Textarea(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'opening_time':forms.TextInput(attrs={'type': 'time', 'class': 'form-control'}),
            'closing_time':forms.TextInput(attrs={'type': 'time', 'class': 'form-control'})
           }

class MenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        exclude = ('restaurant', )

class MenuUpdateForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ('restaurant', 'name',)
