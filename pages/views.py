from django.shortcuts import render

from components.forms import CPUForm

def home(request):
    return render(request, "pages/home.html", {})
