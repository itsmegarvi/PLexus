from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import pickle

model = pickle.load(open('model_pkl1', 'rb'))
# Create your views here.


def index(request):
    return HttpResponse("hello,welcome to my attempt to learn development.")


def predict(request):
    int_features = [request.GET.get('date'), 15]
    outcome = model.predict([[25, 11, 8, 35, 4]])
    return HttpResponse(outcome)
