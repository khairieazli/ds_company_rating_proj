# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 05:31:30 2020

@author: khairie
"""

import requests
import pandas as pd
X_test = pd.read_csv('X_test.csv')

X_test = list(X_test.iloc[1,:])

URL = 'http://127.0.0.1:5000/predict'

headers = {"Content-Type": "application/json"}
data = {"input": X_test}

r = requests.get(URL,headers=headers, json=data)

r.json()