from django.shortcuts import render
from django.views import View
from company.models import Company


class HomePage(View):
    template_name="home-page.html"

    def get(self, request):
        companies=Company.objects.all()
        return render(request, self.template_name)