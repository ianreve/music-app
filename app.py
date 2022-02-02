import re
from flask import Flask, flash, render_template, request, url_for, redirect, abort
import sqlite3 as sql

app = Flask(__name__)

# MusicDB connection 
def musicDB():
    conn = sql.connect('music.db')
    conn.row_factory = sql.Row
    return conn

"home route"
@app.route('/') # set up home route/link to the home page
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/addsongs', methods=['GET', 'POST'])
def addsongs():
    if request.method == 'POST':
        title = request.form['Title']
        artist = request.form['Artist']
        genre = request.form['Genre']

        conn = musicDB()
        cursor = conn.cursor()
        songID = cursor.lastrowid

        cursor.execute('INSERT INTO songs (SongID, Title, Artist, Genre) VALUES (?,?,?,?)', (songID, title, artist, genre))
        conn.commit()
        conn.close()
        return redirect(url_for('songs'))
        
    return render_template('addsongs.html', title = 'Addsongs')

@app.route('/songs')
def songs():
    conn = musicDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM songs")

    getSongs = cursor.fetchall()
    return render_template('songs.html', title = 'Songs', retrieveSongs = getSongs)

def getSongID(recordID):
    conn = musicDB()
    cursor = conn.cursor()
    
    aSong = cursor.execute("SELECT * FROM songs WHERE songID  = ?", (recordID,)).fetchone()
    conn.close()
    if aSong is None:
        abort(404)
    return aSong



"use the route /<int:id>/update" # songID is a placeholder
@app.route('/<int:songID>/update', methods =['GET', 'POST'])
def update(songID): # passed in the primary key songID from the song Table
    songRecord = getSongID(songID)
    if request.method =='POST':
        title = request.form['Title']
        artist = request.form['Artist']
        genre = request.form['Genre']

        conn = musicDB()
        cursor = conn.cursor()
        cursor.execute('UPDATE songs SET title = ?, artist = ?, genre = ?  WHERE songID= ?', ( title, artist, genre, songID))
        conn.commit()
        conn.close()
        return redirect(url_for('songs'))

    return render_template('update.html',title= 'Update Songs' , aSongRecord = songRecord)





if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0', port=8124)