__author__ = 'ianakonkina'
from django import forms


class UserCommentsForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, required=True)
