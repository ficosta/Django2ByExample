from django import forms

class LoginForm(forms.Form):
	"""Formulario de login."""

	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
	"""docstring for UserRegistrationForm"""
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
	
