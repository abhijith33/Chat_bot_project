from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.
import os
import openai

openai.api_key = "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"



def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def chat(request):
    return render(request,'chat.html')

def chatAPI(request):
    if request.method=="POST":
        print(request.prompt)
        response={"this":"that"}
    # response = openai.Completion.create(

    #     model="text-davinci-003",
    #     prompt="",
    #     temperature=1,
    #     max_tokens=256,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )
    
    return JsonResponse(response)