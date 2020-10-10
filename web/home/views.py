from django.shortcuts import render
import pickle
import sys
sys.path.append('C:\\Users\\Abhi\\Envs\\nlp\\lib\\site-packages')
sys.path.append('C:\\Users\\Abhi\\Envs\\nlp')


# Create your views here.
def home(request):
    return render(request,'home.html') 

def predict(request):    
    with open("trained.pickle","rb") as f:
        randomclassifier = pickle.load(f)
    with open("vectorizer.pickle","rb") as t:
        vectorizer = pickle.load(t)
    if request.method == "POST":
        text = request.POST.get('text')
        print(text)
        print("The datastypeof text is",type(text))
        cleared_text = text.replace(r'[?.,!/]',"").lower()
        text_num  = vectorizer.transform([cleared_text])
        prediction = randomclassifier.predict(text_num)

        context = {'predict':prediction,'text':text}
        return render(request,'predict_post.html',context)
    else:
        return render(request,'predict_pre.html')     
