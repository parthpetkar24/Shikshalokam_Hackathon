from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def teacher_dashboard(request):
    return render(request,'teacher.html')

def diet_dashboard(request):
    return render(request,'diet.html')