from flask import Flask, redirect, url_for, request, render_template , jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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
    output = ss+dsi+tsc+cm+tforce+ct+acode+me+rules+wmetric
    return jsonify({'output':output})


if __name__ == '__main__':
    app.run(debug=True)