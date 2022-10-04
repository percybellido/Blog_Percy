from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

    
def portfolio(request):
   return render(request, "portfolio/portfolio.html")

