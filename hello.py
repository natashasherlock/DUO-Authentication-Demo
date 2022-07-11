from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/scam/<gullibility>')
def scam(gullibility):
    gull = int(gullibility)
    if gull > 100:
        return render_template('notscam.html')
    return render_template('carscam.html')


@app.route('/credit')
def credit():
    return render_template('carscam.html')

@app.route('/whatever', methods = ['POST'])
def whatever():
    #if request.method == 'POST':
    user = request.form['fname']
    return render_template('notscam.html', myname=user)
    
