from django import forms
from django.conf import settings
from django.core.mail import send_mail
from .models import *

class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactProfile
		fields = [
			'name',
			'email',
			'message',
			'subject',
		]
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'style':
				"padding: 10px; \
				margin-bottom: 20px; \
				border-bottom: 1px solid grey; \
				outline: none; \
				font-size: 18px; \
				background-color: #c5ccd0;"}),

   
			'email': forms.TextInput(attrs={'class': 'form-control', 'style':
				"padding: 10px; \
				margin-bottom: 20px; \
				border-bottom: 1px solid grey; \
				outline: none; \
				font-size: 18px; \
				background-color: #c5ccd0;"}),
   
			'message': forms.Textarea(attrs={'class': 'form-control', 'style':
				"padding: 10px; \
				margin-bottom: 20px; \
				border-bottom: 1px solid grey; \
				outline: none; \
				font-size: 18px; \
				background-color: #c5ccd0;"}),
   
			'subject': forms.TextInput(attrs={'class': 'form-control', 'style':
				"padding: 10px; \
				margin-bottom: 20px; \
				border-bottom: 1px solid grey; \
				outline: none; \
				font-size: 18px; \
				background-color: #c5ccd0;"}),
		}