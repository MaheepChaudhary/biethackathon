from django.shortcuts import render
import pickle
import sys
from .scrapper import scrapper
sys.path.append('C:\\Users\\Abhi\\Envs\\nlp\\lib\\site-packages')
sys.path.append('C:\\Users\\Abhi\\Envs\\nlp')

# Create your views here.
def home(request):
    return render(request,'index.html')

def search(request):
    return render(request, 'search.html')

def predict(request):    
    with open("/home/rohan/Desktop/biet_hacks/biethackathon/trained.pickle","rb") as f:
        randomclassifier = pickle.load(f)
    with open("/home/rohan/Desktop/biet_hacks/biethackathon/vectroizer.pickle","rb") as t:
        vectorizer = pickle.load(t)
    if request.method == "POST":
        text = request.POST.get('text')
        print(text)
        print("The datastypeof text is",type(text))
        
        #here we will scrape the data from the web
        data = scrapper(text)
        #data = "The stocks are getting so damn high"

        cleared_text = data.replace(r'[?.,!/]',"").lower()
        text_num  = vectorizer.transform([cleared_text])
        prediction = bool(randomclassifier.predict(text_num)[0])
        print(prediction)
        context = {'predict':prediction,'text':text, 'News' : data}
        return render(request,'predict_post.html',context)
    else:
        return render(request,'predict_pre.html')
