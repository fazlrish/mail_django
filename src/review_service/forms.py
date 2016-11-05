
from django.forms import ModelForm
from .models import *

#Registration form based on User model
class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('email','username','password')


#Authorization form based on User model
class UserAuthorizationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

#New Review form based on Review model
class NewReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('text',)