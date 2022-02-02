from flask import Flask, flash, render_template, request, url_for, redirect, abort

app = Flask(__name__)

"home route"
@app.route('/') # set up home route/link to the home page
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/addsongs')
def addsongs():
    return render_template('addsongs.html', title = 'Addsongs')

@app.route('/songs')
def songs():
    return render_template('songs.html', title = 'Songs')


if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0', port=8124)


# mine