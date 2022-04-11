from django.urls import path, include
from django.db import router
from rest_framework import routers
from . import views

router=routers.DefaultRouter()


router.register("signup", views.Signup)
router.register("company", views.Company)
urlpatterns = [
     path("login", views.Login.as_view()),
    path("",include(router.urls)),
]
