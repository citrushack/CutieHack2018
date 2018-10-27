from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class SignUpForm(UserCreationForm):
   first_name = forms.CharField(max_length=30, required=True)
   last_name = forms.CharField(max_length=30, required=True)
   school = forms.CharField(max_length=100, required=True)
   ageOptions = (
      ("",""),
      ("13", "13"),
      ("14", "14"),
      ("15", "15"),
      ("16", "16"),
      ("17", "17"),
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
   genderOptions = (
      ("",""),
      ("Female", "Female"),
      ("Male", "Male"),
      ("Other", "Other"), 
      ("Prefer not to disclose", "Prefer not to disclose"),
      )
   Gender = forms.ChoiceField(choices=genderOptions)
   raceOptions = (
      ("",""),
      ('Asian', 'Asian'), 
      ('Black or African American','Black or African American'), 
      ('Latino or Latin American','Latino or Latin American'), 
      ('Native American', 'Native American'),  
      ('Native Hawaiian or other Pacific Islander','Native Hawaiian or other Pacific Islander'), 
      ('Other','Other'),
      ('Prefer not to diclose', 'Prefer not to disclose'),
      ('Two or more races', 'Two or more races'), 
      ('White', 'White'), 
      )
   Race = forms.ChoiceField(choices=raceOptions)
   major = forms.CharField(max_length=30, required=True)
   studyOptions = (
      ("",""),
      ("1st Year", "1st Year"),
      ("2nd Year", "2nd Year"),
      ("3rd Year", "3rd Year"),
      ("4th Year", "4th Year"),
      ("5th Year or beyond", "5th Year or beyond"),
      ("Prefer not to disclose", "Prefer not to disclose"),
      )
   LevelofStudy = forms.ChoiceField(choices=studyOptions)
   yearOptions = (
      ("",""),
      ("2019", "2019"),
      ("2020", "2020"),
      ("2021", "2021"),
      ("2022", "2022"),
      ("2023", "2023"),
      ("2024", "2024"),
      ("2025", "2025"),
      )
   gradYear = forms.ChoiceField(choices=yearOptions)
   phoneNumber = forms.CharField(max_length=12,required=True)
   Resume = forms.URLField(label='Link to your resume')
   conductBox = forms.BooleanField()
   shareBox = forms.BooleanField()
   dietRestrictions = forms.CharField(max_length=100, required=False)
   meme = forms.URLField(required=False)

   class Meta:
      model = MyUser

      fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'age', 'school', 'major', 'phoneNumber', 'Gender', 'Race', 'LevelofStudy', 'gradYear', 'dietRestrictions', 'conductBox', 'shareBox', 'meme','Resume')

      

