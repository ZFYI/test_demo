from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def count(request):
    text = request.GET['text']
    # print(text)
    count = len(text)
    return render(request,'count.html',{"text":text,"count":count})
