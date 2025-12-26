from django.shortcuts import render

from components.forms import CPUForm

def home(request):
    form = CPUForm()
    return render(request, "pages/home.html", {'form': form})
