from flask import Flask,jsonify

app = Flask(__name__)

d = {
   "ABC" : {"Math": 90, "Science": 88, "English": 91},
   "DEF" : {"Math": 62, "Science": 71, "English": 94},
   "XYZ" : {"Math": 99, "Science": 93, "English": 60},
}

@app.route('/studentMarks')
def marks():
    return jsonify(d)