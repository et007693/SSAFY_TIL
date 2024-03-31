from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    name = forms.CharField(
       widget=forms.TextInput(
          attrs={
            'class':'form-control',
            'placeholder':"메뉴 이름을 작성해 주세요."
          }
       )
    )
    
    price = forms.IntegerField(
       widget=forms.NumberInput(
          attrs={
            'class':'form-control',
          }
       )
    )

    description = forms.CharField(
       widget=forms.Textarea(
          attrs={
            'class':'form-control',
            'placeholder':"메뉴 설명을 작성해 주세요."
          }
       )
    )

    is_vegan = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-label',
            }
        )
    )

    class Meta:
        model = Menu
        fields = '__all__'