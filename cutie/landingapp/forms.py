from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class SignUpForm(UserCreationForm):
   first_name = forms.CharField(max_length=30, required=True)
   last_name = forms.CharField(max_length=30, required=True)
   school = forms.CharField(max_length=100, required=True)
   ageOptions = (
      ("13", "13"),
      ("14", "14"),
      ("15", "15"),
      ("16", "16"),
      ("17", "17 "),
      ("18", "18"),
      ("19", "19"),
      ("20", "20"),
      ("21", "21"),
      ("22", "22"),
      ("23", "23"),
      ("24", "24"),
      ("25", "25"),
      ("26", "26"),
      ("27", "27"),
      ("28", "28"),
      ("29", "29"),
      ("30", "30"),
      ("31", "31"),
      ("32", "32"),
      )
   age = forms.ChoiceField(choices=ageOptions)
   genderOptions = (("a", "Male"), ('b', 'Female'), ("c", "Other"), ("d", "Prefer not to disclose"),)
   Gender = forms.ChoiceField(choices=genderOptions)
   raceOptions = (('a', 'White'), ('b','Black or African American'), ('c', 'Native American'), ('d', 'Asian'), ('e','Native Hawaiian or other Pacific Islander'), ('f','Latino or Latin American'), ('g','Other'), ('h', 'Two or more races'), ('i', 'Prefer not to disclose'), )
   Race = forms.ChoiceField(choices=raceOptions)
   major = forms.CharField(max_length=30, required=True)
   studyOptions = (
      ("a", "1st Year"),
      ("b", "2nd Year"),
      ("c", "3rd Year"),
      ("d", "4th Year"),
      ("e", "5th Year or beyond"),
      ("f", "Prefer not to disclose"),
      )
   LevelofStudy = forms.ChoiceField(choices=studyOptions)
   yearOptions = (
      ("a", "2019"),
      ("b", "2020"),
      ("c", "2021"),
      ("d", "2022"),
      ("e", "2023"),
      ("f", "2024"),
      ("g", "2025"),
      )
   gradYear = forms.ChoiceField(choices=yearOptions)
   phoneNumber = forms.CharField(max_length=12,required=True)
   #Resume = forms.FileField(label='Click to upload file')
   conductBox = forms.BooleanField()
   shareBox = forms.BooleanField()
   dietRestrictions = forms.CharField(max_length=100, required=False)
   meme = forms.CharField(max_length= 200, required=False)

   class Meta:
      model = MyUser
      fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'age', 'school', 'major', 'phoneNumber', 'Gender', 'Race', 'LevelofStudy', 'gradYear', 'dietRestrictions', 'conductBox', 'shareBox', 'meme')

