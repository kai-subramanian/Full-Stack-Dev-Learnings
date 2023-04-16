from flask import Flask,jsonify, render_template

app = Flask(__name__)

d = {
   "ABC" : {"Math": 90, "Science": 88, "English": 91},
   "DEF" : {"Math": 62, "Science": 71, "English": 94},
   "XYZ" : {"Math": 99, "Science": 93, "English": 60},
}

p ={
   "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
   "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
   "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
   "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
                "contribution": "class/object split, subclassing, protected attributes"},
   "Pascal": {"name": "Pascal", "publication_year": 1970,
              "contribution": "modern unary, binary, and assignment operator syntax expectations"},
   "CLU": {"name": "CLU", "publication_year": 1975,
           "contribution": "iterators, abstract data types, generics, checked exceptions"},
}

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/studentMarks')
def marks():
    return jsonify(d)

@app.route('/studentMarks/<student_name>')
def show_marks(student_name):
    if student_name in d:
        return d[student_name] 
    else: 
        return "Not Found"
    
@app.route('/programming')
def programs():
    return jsonify(p)
