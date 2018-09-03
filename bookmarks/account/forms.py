from django import forms

class LoginForm(forms.Form):
	"""Formulario de login."""

	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
