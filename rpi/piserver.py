from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/wheelie', methods = ['POST'])
def create():
    print('super hacker')
    return 'Added sensor!'
@app.route('/home')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
