from django import forms
from django.forms import widgets
from webapp.models import RECORD_STATUS_CHOICES


class RecordForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя')
    mail = forms.EmailField(max_length=100, required=True, label='Email')
    text = forms.CharField(max_length=3000, required=True, widget=widgets.Textarea, label='Текст')