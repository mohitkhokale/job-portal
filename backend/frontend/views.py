from django.shortcuts import render , redirect
from django.views import View
from .forms import CompanyForm, UserRegistrationForm
from company.models import Company
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User


class Login(View):
    template_name = 'login.html'
    form_class = AuthenticationForm
    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('HomePage')
        context ={
            'form':form,
        }
        return render(request, self.template_name, context)

def Logout(request):
    logout(request)
    return redirect('Login')

class Signup(View):
    form_class = UserRegistrationForm

    template_name = 'signup.html'

    def get(self, request):
        signup_form = self.form_class()
        context = {
            'form': signup_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            form.save()
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            email=form.cleaned_data.get('email')
            user_auth = authenticate(username=username, password=password)
            login(request, user_auth)
            return redirect('HomePage')
        else:
            return render(request, self.template_name, {"form":form})

class HomePage(View):
    template_name="home-page.html"
    def get(self, request):
        companies=Company.objects.all()
        context = {
            'companies':companies
        }
        return render(request, self.template_name,context)


class Add_Company(View):
    form_class = CompanyForm
    template_name = "add_companies.html"

    def get(self, request,company_id=None):
        form = self.form_class()
        context = {
            'Add_Company': form
        }
        return render(request,self.template_name,context)

    def post(self, request,company_id=None):
            form = self.form_class(data = request.POST)
            context={}
            if form.is_valid():
                form.save()
                return redirect('HomePage')
            else:  
                context = {
                    'Add_company':form
                } 
                form = self.form_class()
                return render(request,'add_companies.html',context)
      

def Edit_Company(request,company_id=None):
        id = Company.objects.get(pk=company_id)
        form = CompanyForm(request.POST or None,instance=id)
        if form.is_valid():
            form.save()
           
            return redirect('HomePage')
        else:  
            context = {
                'form':form,
            }
            return render(request,'add_companies.html',context)
   

def delete_company(request,company_id=None):
    Company.objects.filter(id=company_id).delete()
    return redirect('HomePage')