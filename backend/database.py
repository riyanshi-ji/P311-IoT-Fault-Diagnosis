import sqlite3
import os

DB_NAME = "data/factory.db"


def create_database():
    # Make sure data folder exists
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id TEXT NOT NULL,
            temperature REAL,
            vibration REAL,
            current REAL,
            status TEXT,
            faults TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


def insert_sensor_data(
    machine_id,
    temperature,
    vibration,
    current,
    status,
    faults
):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sensor_data
        (machine_id, temperature, vibration, current, status, faults)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        machine_id,
        temperature,
        vibration,
        current,
        status,
        faults
    ))

    conn.commit()
    conn.close()


def get_sensor_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sensor_data
        ORDER BY timestamp DESC
    """)

    data = cursor.fetchall()
    conn.close()

    return data


if __name__ == "__main__":
    create_database()