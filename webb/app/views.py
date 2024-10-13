from django.shortcuts import render
# from django.http import HttpResponse    #это если через httpresponse

# Create your views here.


# def index(request):
#     return HttpResponse("<h4>Check</h4>")

def index(request):
    return render(request, 'app/index.html')

# def about(request):
#     return HttpResponse("<h4>Check1</h4>")

def about(request):
    return render(request, 'app/about.html')