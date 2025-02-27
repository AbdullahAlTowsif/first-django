from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, this is my first django page</h1>")

def about(request):
    return HttpResponse("Hello, this is my about page")