from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import collections.abc
collections.Hashable = collections.abc.Hashable

# Create your views here.
# we need to create the function that will be executed once the above url is open

#create an object of chatterbot + # add a default response in logic adapter
bot = ChatBot('chatbot',read_only= False, logic_adapters= [
    {
        'import_path':'chatterbot.logic.BestMatch',
        #'default_response': 'Sorry, I don''t know what that means',
        #'maximum_similarity_threshold': 0.90 #if the response has similarity less than 90% so we send the default answer. for example if we put only name as question the chatbot will answer it's just achatbot because the similarity of name with our knowledge database is higher than 90% otherwise he will answer with the default response, Idon't know
    }])
list_to_train= [
    "hi", #question from user
    "hi, there", #answer from bot,
    "what's your name",
    "I'm just a chatbot",
    "what's your fav food",
    "I like cheese",
    "what's your fav sport",
    "swimming",
    "do you have children",
    "Oh, No"
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    # return a response with html
    return render(request, 'blog/index.html')

def specific(request):
    list =[1,2,3,4]
    return HttpResponse(list)
def getResponse(request):
    userMessage= request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse )

#def article(request, article_id):
#    return HttpResponse(article_id) #allow the users to get specific piece of data by entering the number


#In order to run the html page that we have created and we can show the article id as well if needed
#def article2(request, article_id):
#    return render(request, 'blog/index.html', {'article_id':article_id})