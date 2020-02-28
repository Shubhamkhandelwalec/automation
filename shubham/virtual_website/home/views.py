from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def room(request):
    return render(request,'rooms.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')