from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.
def index(request):
    ctx = {}
    #ctx['active_page'] = 'home'
    return render(request, 'home/index.html', ctx)
