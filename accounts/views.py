from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserSignUpForm
from .forms import UserSignUpFormAddon, UserAdditionalFields
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                user_form.add_error(
                    None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "Unable to log you in at this time!")
    else:
        user_form = UserSignUpForm()

    args = {'user_form': user_form}
    return render(request, 'sign-up.html', args)


@login_required
def edit_user(request):
    """A view that allows a user to add and edit
    additional information for their profile"""

    if request.method == 'POST':
        user_form = UserSignUpFormAddon(request.POST, instance=request.user)
        profile_form = UserAdditionalFields(
            request.POST, request.FILES, instance=request.user.usercreate)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, "Your profile has successfully been updated!")
            return redirect(reverse('profile'))
        else:
            messages.error(
                request, "Unable to update. Please rectify the problems below")
    else:
        user_form = UserSignUpFormAddon(instance=request.user)
        profile_form = UserAdditionalFields(instance=request.user.usercreate)
    args = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'edit_user.html', args)
