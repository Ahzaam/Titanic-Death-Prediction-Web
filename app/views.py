from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from app.predict import model_prediction
from .models import Predictions
# Create your views here.

def hi(request):
    return HttpResponse('<h1>Pyhton Django Titanic Death prediction Website <a href="/home">Home</a></h1>')

def home(request):
    return render(request, 'home.html')

def predict(request):
    result = int(model_prediction(request)[0])
    return JsonResponse({'result' :result }, status=200)

def history(request):
    hisdata = Predictions.objects.all()
    print(hisdata)
    return render(request, 'history.html', {"data" : hisdata})
