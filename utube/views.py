from django.shortcuts import render

# Create your views here.
def shorts(request):
    return render(request,'shorts.html')
def like(request):
    return render(request,'like.html')