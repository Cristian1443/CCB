from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Datos de ejemplo (en un sistema real usarías una base de datos)
users = {
    'gestora': {'password': 'password123', 'role': 'admin'}
}

events = []
instructors = []

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username]['password'] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Credenciales inválidas", 401
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/api/events', methods=['GET', 'POST'])
def handle_events():
    if request.method == 'POST':
        new_event = request.json
        events.append(new_event)
        return jsonify(new_event), 201
    return jsonify(events)

@app.route('/api/instructors', methods=['GET', 'POST'])
def handle_instructors():
    if request.method == 'POST':
        new_instructor = request.json
        instructors.append(new_instructor)
        return jsonify(new_instructor), 201
    return jsonify(instructors)

if __name__ == '__main__':
    app.run(debug=True)