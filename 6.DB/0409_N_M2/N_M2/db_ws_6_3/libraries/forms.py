from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('nickname', )

class BookFrom(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'