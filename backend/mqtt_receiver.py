
import json
import ssl
import paho.mqtt.client as mqtt

from config import (
    HIVEMQ_HOST,
    HIVEMQ_PORT,
    HIVEMQ_USERNAME,
    HIVEMQ_PASSWORD,
    MQTT_TOPIC
)

from backend.database import insert_sensor_data
from backend.fault_detector import diagnose_fault


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to HiveMQ!")
        client.subscribe(MQTT_TOPIC, qos=1)
        print("Subscribed to:", MQTT_TOPIC)
    else:
        print("Connection failed:", reason_code)


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        machine_id = data["machine_id"]
        temperature = float(data["temperature"])
        vibration = float(data["vibration"])
        current = float(data["current"])

        status, faults = diagnose_fault(
            temperature, vibration, current
        )

        print("\n--- MACHINE DIAGNOSIS ---")
        print("Machine:", machine_id)
        print("Temperature:", temperature)
        print("Vibration:", vibration)
        print("Current:", current)
        print("Status:", status)
        print("Faults:", faults if faults else "None")

        faults_text = ", ".join(faults)

        insert_sensor_data(
            machine_id,
            temperature,
            vibration,
            current,
            status,
            faults_text
        )

        print("Data saved to database!")

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as e:
        print("Invalid sensor message:", e)


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="p311-receiver"
)

client.username_pw_set(
    HIVEMQ_USERNAME,
    HIVEMQ_PASSWORD
)

client.tls_set(
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.on_connect = on_connect
client.on_message = on_message

print("Connecting to HiveMQ...")
client.connect(HIVEMQ_HOST, HIVEMQ_PORT, 60)

client.loop_forever()
