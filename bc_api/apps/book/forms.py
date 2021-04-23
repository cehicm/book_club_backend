from django import forms

class BookForm(forms.Form):
    name = forms.CharField(max_length=5, required=True)