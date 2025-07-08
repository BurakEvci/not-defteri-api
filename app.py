from flask import Flask, request, jsonify

app = Flask(__name__)

# Geçici veri — sonra PostgreSQL'e bağlayacağız
notes = []

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    if not data or "content" not in data:
        return jsonify({"error": "Lütfen 'content' alanını gönderin."}), 400
    note = {
        "id": len(notes) + 1,
        "content": data["content"]
    }
    notes.append(note)
    return jsonify(note), 201

@app.route("/")
def home():
    return "Not Defteri API Çalışıyor!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
