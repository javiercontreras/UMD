from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
# Create your views here.

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect("user:profile")
    else:
        # we populate the user form 
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "profile.html", {"u_form":user_form, "p_form": user_profile_form})