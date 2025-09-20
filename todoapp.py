from flask import Flask, request, jsonify
import pyodbc
import os

app = Flask(__name__)

# Connection string from App Service settings
db_conn_str = os.environ.get("DB_CONN")

def get_db_connection():
    conn = pyodbc.connect(db_conn_str)
    return conn

@app.route("/todos", methods=["GET", "POST"])
def todos():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        item = request.json.get("task")
        cursor.execute("INSERT INTO Todos (Task) VALUES (?)", (item,))
        conn.commit()
        return jsonify({"message": "Task added"}), 201

    cursor.execute("SELECT Task FROM Todos")
    tasks = [row[0] for row in cursor.fetchall()]
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)