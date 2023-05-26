from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("This is home page")
    context = {
        "variable1":"news title",
        "variable2":"newscontent"
    }
    return render(request, 'home.html', context)

def about(request):
    return HttpResponse("This is about page")

def news(request):
    return HttpResponse("This is news page")

def contact(request):
    return HttpResponse("This is contact page")

