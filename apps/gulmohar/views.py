from django.shortcuts import render

# Create your views here.


def newPage(request):
    return render(request, "gulmohar/landingPage.html")

def landing3(request):
    return render(request, "gulmohar/rental.html")

def landing4(request):
    return render(request, "gulmohar/landing4.html")    
def landing5(request):
    return render(request, "gulmohar/landing5.html")

def landing6(request):
    return render(request, "gulmohar/landing6.html")

def landing7(request):
    return render(request, "gulmohar/landing7.html")

def booking(request):
    return render(request, "gulmohar/booking_2.html")