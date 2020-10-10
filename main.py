from __init__ import *
from preprocessing import preprocessing

df = pd.read_csv('Data.csv',encoding= 'unicode_escape')

headlines = np.array(preprocessing(df))
labels = np.array([x for x in df['Label']])

print(labels.shape)
print(headlines.shape)

vectorizer = CountVectorizer(ngram_range=(2,2))
vectorizer.fit(headlines)
dataset = vectorizer.transform(headlines)

train = dataset[:3800]
test = dataset[3800:]
randomclassifier = RandomForestClassifier(n_estimators = estimators)
'''
print("Training is going on")
randomclassifier.fit(train,labels[:3800])
with open("trained.pickle","wb") as f:
    pickle.dump(randomclassifier,f)

with open("vectroizer.pickle","wb") as z:
    pickle.dump(vectorizer,z)
'''
'''
with open("trained.pickle","rb") as ri:
    randomclassifier = pickle.load(ri)

predict = randomclassfier.predict(test[1])
print(predict)
#evaluating the randomclassifier
print("Evaluation is happening")
prediction = randomclassifier.predict(test)
print(accuracy_score(prediction,labels[3800:]))    

'''
with open("trained.pickle","rb") as ri:
    randomclassifier = pickle.load(ri)

print(headlines[3801])
print(randomclassifier.predict(test[1]))