from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict={"text":"Hello world!",
             "number":80           }
    return render(request,"firstapp/index.html",context=my_dict)
def other(request):
    return render(request,"firstapp/other.html")
def relative(request):
    return render(request,"firstapp/raltive.html")
