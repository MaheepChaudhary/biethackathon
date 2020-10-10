#reading the data
from __init__ import *

def preprocessing(dataframe):
    headlines = []
    for row in dataframe.iterrows():
        headline = []
        row[1].iloc[2:27] = (row[1].iloc[2:27]).str.replace('[?.!:,""]',"")  
        for i in row[1].iloc[2:27]:
            headline.append(str(i).lower())
        headlines.append(" ".join(headline)) 
    return headlines



