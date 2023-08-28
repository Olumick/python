from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# import spacy.cli 
# spacy.cli.download("en_core_web_md")
# ChatterBotCorpusTrainer is to train bot on thousands of conversation from other people
from chatterbot.trainers import ChatterBotCorpusTrainer

# create the object of the ChatBot
# read_only=False means we want the bot to ready only but also to respond to the user
# logic_adapters determine what the chatbot will be used for i.e., 
# to solve maths problems or simple conversation
# bot = ChatBot('chatbot',read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])
bot = ChatBot('chatbot',read_only=False,
              logic_adapters=[
                 { 
                     'import_path':'chatterbot.logic.BestMatch',
                    #  ChatterBotCorpusTrainer has its own default response
                    #  'default_response':'Sorry, I don\'t know that means',
                    #  'maximum_similarity_threshold':0.90
                  }
                  ])

# we need to train/teach the chatbot to make it functional
list_to_train = [
    "hi",
    "hi, there",
    "What's your name",
    "I'm just a chatbot",
    "What's is your fav food",
    "I like beans and platain", 
    "What's your fav sport",
    "Swimming and football",
    "Do you have children",
    "No",

]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')

# the ListTrainer will take a list and train the chatbot to respond with question and answer
# create the object of the ListTrainer and should take the bot object

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)



# def index(request):
#     return HttpResponse('This is first url')

def specific(request):
    # return HttpResponse('This is machine learning url')

    # number = 55
    # return HttpResponse(number)

    list = [1,2,3,4,5]
    return HttpResponse(list)

def machine_learning(request):
    x = 10
    y = 20
    z = x + y
    return HttpResponse(z)

# allow user to pass a parameter   
# def article(request,article_id):
#     return render(request,'virtual_assistant/index.html',{'article_id': article_id})

# ==========================================================

def index(request):
    return render(request, 'chatterbot_app/index.html')

# def article(request,article_id):
#     return render(request,'chatterbot_app/index.html',{'article_id': article_id})


# get the text from user from the frontend (index.html) and store it in python
# the HttpResponse will send it back to data in done() function in the frontend
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    # since bot has been trained, we need to hte message from the bot
    # convert str so the app doesn't crash
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
    # return HttpResponse(userMessage)


