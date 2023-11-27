from flask import Flask, render_template, jsonify
app = Flask(__name__)

langs = [
    {
        'Language':'Python',
        'Level':'Advanced',
        'Frameworks':['Django', 'Flask']
    },
    {
        'Language':'HTML',
        'Level':'Expert'
    },
    {
        'Language' : 'CSS',
        'Level' : 'Expert'
    },
    {
        'Language' : 'Javascript',
        'Level' : 'Expert'
    }
]

@app.route("/")
def hello():
    return render_template('index.html', langs = langs)

@app.route("/api/skills")
def skills():
    return jsonify(langs)

if __name__=='__main__':
    app.run(debug=True)
