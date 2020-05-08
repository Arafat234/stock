from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
# from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def help(request):
    return render(request,'help.html')

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'registration/signup.html',context)

# @login_required
# def viewprofile(request):
#     if request.method == "POST":
#         u_form = UserUpdateForm(request.POST, instance = request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
#         # a = User.objects.filter(username = u_form['username'].value()).exists()
#         # print(a)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect('viewprofiles')
#
#     else:
#         u_form = UserUpdateForm(instance = request.user)
#         p_form = ProfileUpdateForm(instance = request.user.profile)
#
#
#     context = {
#         'u_form' : u_form,
#         'p_form' : p_form
#     }
#     return render(request,'registration/userprofile.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            print(p_form)
            messages.success(request,'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,

    }

    return render(request, 'registration/userprofile.html', context)


@login_required
def deleteprofile(request):
    user_id = request.user.pk
    User.objects.filter(pk=user_id).delete()
    return redirect('home')
    #return render(request,'home.html')
