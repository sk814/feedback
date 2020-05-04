from django.shortcuts import render,get_object_or_404
from .forms import FeedbackForm
from .models import Feedback


# Create your views here.

def feedback(request):
    if request.method == 'GET':
        print("Testing1-1")
        return render(request, 'feedbackformapp/home.html', {'form':FeedbackForm()})
    else:
        try:
            print("Testing1-2.1")
            form = FeedbackForm(request.POST)
            print(request.POST)
            print("Testing1-2.2")
            user = form.save(commit=False)
            print("Testing1-2.3")
            user.company = request.POST['company']
            user.Product = request.POST['Product']
            user.Service = request.POST['Service']
            user.Employee = request.POST['Employee']
            user.Value = request.POST['Value']
            user.Recommendable = request.POST['Recommendable']
            user.review = request.POST['review']
            user.total= int(request.POST['Product']) + int(request.POST['Service']) + int (request.POST['Employee']) + int (request.POST['Value']) + int(request.POST['Recommendable'])
            user.save()
            print("Testing1-2")
            return render(request, 'feedbackformapp/thanks.html', {'form':user})


        except ValueError:
            return render(request, 'feedbackformapp/home.html', {'form': FeedbackForm(), 'error': 'Bad data passed in. Try again.'})




