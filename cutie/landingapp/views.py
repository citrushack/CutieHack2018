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
	return render(request, 'index.html', context={}, ) #context is empty for now: this is if we want to incorporate data into our landing page

def profile(request): #implement the case when user is not logged in redirect to login page
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
            user.profile.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.profile.school = form.cleaned_data.get('school')
            user.profile.major = form.cleaned_data.get('major')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#2 form method incomplete
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, ('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, ('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })