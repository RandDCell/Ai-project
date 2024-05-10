from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

# Database initialization
def init_db():
    conn = sqlite3.connect('database/crud_operations.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Create
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = sqlite3.connect('database/crud_operations.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', (name, email))
        conn.commit()
        conn.close()
       return redirect(url_for('index'))
    return render_template('form.html')

# Read
@app.route('/')
def index():
    conn = sqlite3.connect('database/crud_operations.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users''')
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

# Update
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect('database/crud_operations.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute('''UPDATE users SET name=?, email=? WHERE id=?''', (name, email, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute('''SELECT * FROM users WHERE id=?''', (id,))
    user = cursor.fetchone()
    conn.close()
    return render_template('form.html', user=user)

# Delete
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database/crud_operations.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM users WHERE id=?''', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
