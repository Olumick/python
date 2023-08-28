from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# create the object of the ChatBot
# read_only=False means we want the bot to ready only but also to respond to the user
# logic_adapters determine what the chatbot will be used for i.e., 
# to solve maths problems or simple conversation
bot = ChatBot('chatbot',read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])

def index(request):
    return render(request,'virtual_assistant/index.html')

def specific(request):
    return HttpResponse('list')
    
# def article(request,article_id):
#     return render(request,'virtual_assistant/index.html',{'article_id': article_id})

def getResponse(request):
    # get the text from user from the frontend (index.html) and store it in python
    # the HttpResponse will send it back to data in done() function in the frontend
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)