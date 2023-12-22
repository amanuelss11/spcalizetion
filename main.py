from flask import Flask, render_template

app = Flask(__name__)
thisdict =[ 
{
"brand": "Ford",
"model": "Mustang",
"year": 1964
},
{"brand": "Fyyord",
"model": "Musyytang",
"year": 19674
}
]
@app.route("/")
def hello_world():
    return render_template('sol.html',sl=thisdict )
app.run(host='0.0.0.0',debug=True) 