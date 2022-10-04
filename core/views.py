from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name="core/home.html"
    
    

class AboutPageView(TemplateView):
    template_name="core/about.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']="Percy Bellido Gomez"
        return context
    
    
def portfolio(request):
   return render(request, "core/portfolio.html")

def blog(request):
    return render(request, "core/blog.html")
    
def contact(request):
    return render(request, "core/contact.html")
