from django.shortcuts import render

# Create your views here.
def movie(request):
    return render(request,'movie.html')
def series(request):
    return render(request,'series.html')