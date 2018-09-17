from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from .models import Profile



#Hey Jerry: over here: required=True and add additional fields that you added in models.py
class SignUpForm(UserCreationForm):
   first_name = forms.CharField(max_length=30, required=True, help_text='fname')
   last_name = forms.CharField(max_length=30, required=True, help_text='lname')
   date_of_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
   school = forms.CharField(max_length=100, required=True, help_text='school')
   major = forms.CharField(max_length=30, required=True, help_text='major')
   phoneNumber = forms.ChoiceField(required=True,help_text="Format: ***********; digits only")
   genderOptions = (("a", "male"), ('b', 'female'), ("c", "non-binary"), ("d", "transgender"), ('e', 'other'), ('f', "I prefer not to answer"))
   Gender = forms.ChoiceField(choices=genderOptions)
   raceOptions = (('a', 'American Indian or Alaskan Native'), ('b','Asian or Pacific Islander'), ('c', 'Black or African American'), ('d', 'Hispanic'), ('e','White / Caucasian'), ('f','Multiple ethnicity / Other'), ('g','I prefer not to answer'))
   Race = forms.ChoiceField(choices=raceOptions)
   studyOptions = (
      ("a", "Freshman"),
      ("b", "Sophomore"),
      ("c", "Junior"),
      ("d", "Senior"),
      ("e", "Graduate Student"),
      )
   LevelofStudy = forms.ChoiceField(choices=studyOptions)
   yearOptions = (
      ("a", "2018"),
      ("b", "2019"),
      ("c", "2020"),
      ("d", "2021"),
      ("e", "2022"),
      )
   gradYear = forms.ChoiceField(choices=yearOptions)
   dietOptions = (
      ("a", "Vegetarian"),
      ("b", "Vegan"),
      ("c", "Gluten Free"),
      ("d", "Kosher"),
      ("e", "Diary Free"),
      ("f", "None")
      )
   dietRestrictions = forms.ChoiceField(choices=dietOptions)
   Resume = forms.FileField()
   conductBox = forms.BooleanField()
   shareBox = forms.BooleanField()
   questions = forms.CharField(max_length= 200)

   class Meta:
      model = MyUser
      fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'school', 'major', 'phoneNumber', 'Gender', 'Race', 'LevelofStudy', 'gradYear', 'dietRestrictions', 'Resume', 'conductBox', 'shareBox', 'questions')
# User model only has email and password as its fields
# and profile has everything else

# So, the SignUpForm which uses the user model doesn't have the fields.
# That's why we are writign them out manually in line 7~11.

# if we use a separate form: profileForm: the fields are already declaraed for profile model in the 
# models.py. so we don't need to declare them again if we use a separate form for the profile model.


### going to use profile form

class ProfileForm(forms.ModelForm):
     class Meta:
         model = Profile
         fields = ('user', 'first_name', 'last_name', 'date_of_birth','school', 'major','phoneNumber' , 'Gender', 'Race', 'LevelofStudy', 'gradYear', 'dietRestrictions', 'Resume', 'conductBox', 'shareBox', 'questions')
         labels = {
            'LevelofStudy': ('Class Standing'),
            'gradYear': ('Expected Graduation Year'),
            'dietRestrictions' : ('Dietary Restictions'),
            'conductBox' : ('I have read and agree to the ​MLH Code of Conduct​'),
            'shareBox' : ('​I authorize you to share my application/registration information for event administration, ranking, MLH administration, pre- and post-event informational e-mails, and occasional messages about hackathons in-line with the ​MLH Privacy Policy​. I agree to the terms of both the ​MLH Contest Terms and Conditions​ and the ​MLH Privacy Policy​.'),
            'questions': ('Anything else you would like to let us know?')
         }