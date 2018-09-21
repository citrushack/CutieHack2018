from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
# Create your views here.

''' test
def index(request):
    return HttpResponse("You're at the index.")
'''
def index(request):
	return render(request, 'index.html', context={}, ) #context is empty unless we want to incorporate data into our landing page

def profile(request): #implement the case when user is not logged in redirect to login page  if not request.user.is_authenticated: return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	return render(request, 'profile.html', context={}, )

def live(request):
    return render(request, 'live.html', context={}, )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data.get('email')
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.age = form.cleaned_data.get('age')
            user.profile.school = form.cleaned_data.get('school')
            user.profile.major = form.cleaned_data.get('major')
            user.profile.phoneNumber = form.cleaned_data.get('phoneNumber')
            user.profile.gender = form.cleaned_data.get('Gender')
            user.profile.race = form.cleaned_data.get('Race')
            user.profile.LevelofStudy = form.cleaned_data.get('LevelofStudy')
            user.profile.gradYear = form.cleaned_data.get('gradYear')
            user.profile.dietRestrictions = form.cleaned_data.get('dietRestrictions')
            user.profile.Resume = form.cleaned_data.get('Resume')
            user.profile.shareBox = form.cleaned_data.get('shareBox')
            user.profile.conductBox = form.cleaned_data.get('conductBox')
            user.profile.questions = form.cleaned_data.get('questions')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})