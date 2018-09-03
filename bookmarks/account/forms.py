from django import forms
from django.con.auth.models import User

class LoginForm(forms.Form):
	"""Formulario de login."""

	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
	"""docstring for UserRegistrationForm"""
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd ['password2']:
			raise forms.ValidationError('Passwords don\'t match')
		return cd['password2']
