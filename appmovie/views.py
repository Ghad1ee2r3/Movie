from django.shortcuts import render

# Create your views here.
from django.http import Http404 , JsonResponse
from django.shortcuts import render, redirect
import requests

# Create your views here.
def omdb_test(request):
    key="2d7bd6a0"
    url= f"http://www.omdbapi.com/?apikey={key}&s=avengers"  #lord of the rings
    response=requests.get(url).json()
    context={
     "resp":response,
    }
    return render (request , 'omdb.html' ,context)



    #return JsonResponse(response)
    #print(response.json())
    #pass
