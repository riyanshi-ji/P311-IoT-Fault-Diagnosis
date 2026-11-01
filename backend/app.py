
from flask import Flask, jsonify
from flask_cors import CORS

from backend.database import get_sensor_data

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "P311 IoT Fault Diagnosis API is running"
    })


@app.route("/api/latest")
def latest_data():

    data = get_sensor_data()

    if not data:
        return jsonify({
            "message": "No sensor data available"
        }), 404

    row = data[0]

    return jsonify({
        "id": row[0],
        "machine_id": row[1],
        "temperature": row[2],
        "vibration": row[3],
        "current": row[4],
        "status": row[5],
        "faults": row[6].split(", ") if row[6] else [],
        "timestamp": row[7]
    })


@app.route("/api/history")
def history():

    data = get_sensor_data()

    result = []

    for row in data[:30]:

        result.append({
            "id": row[0],
            "machine_id": row[1],
            "temperature": row[2],
            "vibration": row[3],
            "current": row[4],
            "status": row[5],
            "faults": row[6].split(", ") if row[6] else [],
            "timestamp": row[7]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
