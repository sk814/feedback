from django.shortcuts import render

# Create your views here.

def feedback(request):
    return render(request, 'feedbackformapp/home.html')



