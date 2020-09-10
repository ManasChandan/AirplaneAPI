from pickle5 import pickle

Pkl_Filename = 'Pickle_RL_Model.pkl'

with open(Pkl_Filename, 'rb') as file:
    final_model = pickle.load(file)

import  numpy as np

input = [[49.223744,14,22,71.285324,0.272118,78.04,2,31335.47682,3,0.424352]]
pred = final_model.predict(input)

print(pred)