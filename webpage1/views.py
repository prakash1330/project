from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'/home/prakash/website/mywebsite/webpage1/templates/home.html')