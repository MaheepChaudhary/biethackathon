import sys
sys.path.append('C:\\Users\\Abhi\\Envs\\nlp\\lib\\site-packages')
sys.path.append('C:\\Users\\Abhi\\Envs\\nlp')

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
import pickle
estimators = 200
