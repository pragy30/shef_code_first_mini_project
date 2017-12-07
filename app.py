from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def metoo(): 
    return render_template('index.html')

if __name__=='__main__':
    app.run()

# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
# app.run(debug=True)
