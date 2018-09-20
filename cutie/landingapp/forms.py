from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class SignUpForm(UserCreationForm):
   first_name = forms.CharField(max_length=30, required=True, help_text='fname')
   last_name = forms.CharField(max_length=30, required=True, help_text='lname')
   email = forms.EmailField(max_length=40, required=True, help_text='e-mail')
   confirmEmail = forms.EmailField(max_length=40, required=True, help_text='confirm e-mail')
   password1 = forms.CharField(max_length=32, widget=forms.PasswordInput, help_text='password')
   password2 = forms.CharField(max_length=32, widget=forms.PasswordInput, help_text='confirm password')
   school = forms.CharField(max_length=100, required=True, help_text='school')
   ageOptions = (
      ("a", "13"),
      ("b", "14"),
      ("c", "15"),
      ("d", "16"),
      ("e", "17 "),
      ("f", "18"),
      ("g", "19"),
      ("h", "20"),
      ("i", "21"),
      ("j", "22"),
      ("k", "23"),
      ("l", "24"),
      ("m", "25"),
      ("n", "26"),
      ("o", "27"),
      ("p", "28"),
      ("q", "29"),
      ("r", "30"),
      ("s", "31"),
      ("t", "32"),
      )
   age = forms.ChoiceField(choices=ageOptions)
   genderOptions = (("a", "male"), ('b', 'female'), ("c", "Other"), ("d", "Prefer not to disclose"),)
   Gender = forms.ChoiceField(choices=genderOptions)
   raceOptions = (('a', 'White'), ('b','Black or African American'), ('c', 'Native American'), ('d', 'Asian'), ('e','Native Hawaiian or other Pacific Islander'), ('f','Latino or Latin American'), ('g','Other'), ('h', 'Two or more races'), ('i', 'Prefer not to disclose'), )
   Race = forms.ChoiceField(choices=raceOptions)
   major = forms.CharField(max_length=30, required=True, help_text='major')
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
   phoneNumber = forms.CharField(max_length=12,required=True,help_text="Phone Number: 123 456 7890")
   Resume = forms.FileField()
   conductBox = forms.BooleanField()
   shareBox = forms.BooleanField()
   dietRestrictions = forms.CharField(max_length=100)
   meme = forms.CharField(max_length= 200)

   class Meta:
      model = MyUser
      fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'age', 'school', 'major', 'phoneNumber', 'Gender', 'Race', 'LevelofStudy', 'gradYear', 'dietRestrictions', 'Resume', 'conductBox', 'shareBox', 'meme')

