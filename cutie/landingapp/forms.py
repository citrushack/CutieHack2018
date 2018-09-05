from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='fname')
	last_name = forms.CharField(max_length=30, required=False, help_text='lname')
	date_of_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	school = forms.CharField(max_length=100, required=False, help_text='school')
	major = forms.CharField(max_length=30, required=False, help_text='major')

	class Meta:
		model = MyUser
		fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'school', 'major')


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('url', 'location', 'company')