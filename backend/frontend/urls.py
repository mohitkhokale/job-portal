from django.urls import path
from . import views

urlpatterns = [
    path("home", views.HomePage.as_view(), name="HomePage"),
    path("", views.Login.as_view(), name="Login"),
    path("logout", views.Logout, name="Logout"),
    path("signup", views.Signup.as_view(), name="signup"),
    
    path("add_company", views.Add_Company.as_view(), name="add_company"),
    path("add_company/<int:company_id>", views.Edit_Company, name="edit_company"),
    path("delete_company/<int:company_id>", views.delete_company, name="delete_company"),
]
