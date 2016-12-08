from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic

from models import User
from review.models import Review
from accounts.forms import UserRegistrationForm, UserAuthorizationForm
# Registration page View
def registration_view(request):
    if (request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username', None),
                                            email=form.cleaned_data.get('email',None),
                                            password=form.cleaned_data.get('password', None))
            user.save()
            return HttpResponseRedirect("/accounts/login/")

    else:
        form = UserRegistrationForm()
        template_name = "accounts/registration.html"
        return render(request, template_name, {'form': form})

#Logout page View
def LogOutView(request):
    logout(request)
    return HttpResponseRedirect("/")

# Users page View
class UserListView(generic.ListView):
    template_name = "accounts/userList.html"
    context_object_name = "userList"

    def get_queryset(self):
        return User.objects.all()

# Categories page View
def UserDetailView(request, user_id):
    template_name = "/user_procession_service/userDetail.html"
    user = User.objects.get(pk=user_id)
    reviews = Review.objects.filter(user=user_id)
    return render(request, template_name, {'user': user, 'reviews': reviews})