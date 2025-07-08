from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)


# Veritabanı bağlantısı
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )
    return conn

@app.route('/notes', methods=['GET'])
def get_notes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, content FROM notes ORDER BY id ASC;')
    rows = cur.fetchall()
    cur.close()
    conn.close()

    notes = [{"id": row[0], "content": row[1]} for row in rows]
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({"error": "İçerik boş olamaz"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO notes (content) VALUES (%s) RETURNING id;', (content,))
    note_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": note_id, "content": content}), 201


@app.route("/")
def home():
    return "Not Defteri API Çalışıyor!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
