from flask import Flask, request, render_template

@app.route('/home')
def home():
    return render_template('index.html')
