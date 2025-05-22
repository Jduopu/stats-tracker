"""
The main handler for the project
Jon Duopu
May. 22nd, 2025
"""

# VARIABLES
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# FUNCTIONS
def init_db(): # Create the database
  connection = sqlite3.connect("database.db")
  cursor = connection.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS Players(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  position TEXT,
  touchdowns INTEGER,
  yards INTEGER,
  tackles INTEGER
)''')
  connection.commit()
  connection.close()

@app.route('/')
def index():
  return redner_template("index.html")

@app.route('/players', methods = ['GET','POST'])
def players():
  connection = sqlite3.connect("database.db")
  cursor = connection.cursor()
  if request.method == 'POST':
        data = request.get_json()
        c.execute('INSERT INTO players (name, position, touchdowns, yards, tackles) VALUES (?, ?, ?, ?, ?)',
                  (data['name'], data['position'], data['touchdowns'], data['yards'], data['tackles']))
        conn.commit()
        return jsonify({'status': 'success'})
    else:
        c.execute('SELECT * FROM players')
        rows = c.fetchall()
        players = [dict(id=row[0], name=row[1], position=row[2], touchdowns=row[3], yards=row[4], tackles=row[5]) for row in rows]
        return jsonify(players)

def main():
  init_db()
  app.run(debug=True)
  
# FUNCTION CALLS
main()
