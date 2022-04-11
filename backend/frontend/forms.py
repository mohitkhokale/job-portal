from xml.parsers.expat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from company.models import Company


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields= ['username','first_name','last_name','email']


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields= '__all__'