from django.shortcuts import render
from django.http import HttpResponse

def start(request):
    #return HttpResponse('HELLO FROM POSTS')

    return render(request,'bone/start.html',{'title': 'new posts'})
