from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure Flask App (No DB)"

@app.route("/todos", methods=["GET"])
def todos():
    return jsonify(["Task1", "Task2"])
