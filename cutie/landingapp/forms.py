from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

#Hey Jerry: over here: required=True and add additional fields that you added in models.py
class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='fname')
	last_name = forms.CharField(max_length=30, required=False, help_text='lname')
	date_of_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	school = forms.CharField(max_length=100, required=False, help_text='school')
	major = forms.CharField(max_length=30, required=False, help_text='major')

	class Meta:
		model = MyUser
		fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'school', 'major')

# User model only has email and password as its fields
# and profile has everything else

# So, the SignUpForm which uses the user model doesn't have the fields.
# That's why we are writign them out manually in line 7~11.

# if we use a separate form: profileForm: the fields are already declaraed for profile model in the 
# models.py. so we don't need to declare them again if we use a separate form for the profile model.


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('url', 'location', 'company')