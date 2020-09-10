from flask import Flask, redirect, url_for, request, render_template , jsonify
from flask_cors import CORS
from pickle5 import pickle

app = Flask(__name__)
CORS(app)

def prediction(features):
    pred = final_model.predict(features)
    return pred[0]

@app.route('/predict' , methods =['GET','POST'])
def posting():
    jsonRequest = request.json
    print(jsonRequest)
    ss = float(jsonRequest['ss'])
    dsi = float(jsonRequest['dsi'])
    tsc = float(jsonRequest['tsc'])
    cm = float(jsonRequest['cm'])
    tforce = float(jsonRequest['tforce'])
    ct = float(jsonRequest['ct'])
    acode = float(jsonRequest['acode'])
    me = float(jsonRequest['me'])
    rules = float(jsonRequest['rules'])
    wmetric = float(jsonRequest['wmetric'])
    features = [[ss,dsi,tsc,cm,tforce,ct,acode,me,rules,wmetric]]
    output = prediction(features=features)
    return jsonify({'output':str(output)})


if __name__ == '__main__':
    Pkl_Filename = 'Pickle_RL_Model.pkl'
    with open(Pkl_Filename, 'rb') as file:
        final_model = pickle.load(file)
    app.run(debug=True)


#testjson =
#{"ss":49.223744,"dsi":14,"tsc":22 ,"cm":71.285324,"tforce":0.272118 ,"ct":78.04 , "acode":2 , "me":31335.47682 , "rules":3 , "wmetric":0.424352}