from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/cloneg1')

@app.route('/cloneg1')
def cloneg1():
    return render_template('cloneg1.html')

if __name__ == '__main__':
    app.run(debug=True)
