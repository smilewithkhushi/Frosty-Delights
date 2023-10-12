from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime

# Create your views here.
def index(request):

    #used to pass values and variables to page and render it
    context= {
        "variable1" : "im khushi",
        "variable2" : "Khushi lvoes to code"
    }
    return render(request, "index.html", context)

    #used to render a webpage
    #return render(request, 'index.html')

    # return HttpResponse("Hello there, this is home page!")
    #this is used to directly render a msg 

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email=request.POST.get('email')
        brand=request.POST.get('brand')
        flavour=request.POST.get('flavour')
        extraInformation=request.POST.get('extraInformation')
        contact=Contact(username=username, email=email, brand=brand, flavour=flavour, extraInformation=extraInformation, date= datetime.today() )
        contact.save()
    return render(request, "contact.html") 


def services(request):
    return render(request, "services.html")
