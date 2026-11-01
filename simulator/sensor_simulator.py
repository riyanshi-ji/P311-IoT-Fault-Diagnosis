import paho.mqtt.client as mqtt
import json
import random
import time
import ssl

from config import (
    HIVEMQ_HOST,
    HIVEMQ_PORT,
    HIVEMQ_USERNAME,
    HIVEMQ_PASSWORD,
    MQTT_TOPIC
)


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="p311-sensor"
)

client.username_pw_set(
    HIVEMQ_USERNAME,
    HIVEMQ_PASSWORD
)

client.tls_set(
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)

print("Connecting to HiveMQ Cloud...")

client.connect(
    HIVEMQ_HOST,
    HIVEMQ_PORT,
    60
)

client.loop_start()

print("Connected to HiveMQ!")
print("Publishing sensor data...\n")


while True:

    temperature = round(random.uniform(50, 75), 2)
    vibration = round(random.uniform(10, 40), 2)
    current = round(random.uniform(3, 6), 2)

    # Generate a fault sometimes
    if random.random() < 0.2:
        temperature = round(random.uniform(85, 100), 2)
        vibration = round(random.uniform(70, 95), 2)
        current = round(random.uniform(8, 10), 2)

    data = {
        "machine_id": "MACHINE_01",
        "temperature": temperature,
        "vibration": vibration,
        "current": current
    }

    message = json.dumps(data)

    result = client.publish(
        MQTT_TOPIC,
        message,
        qos=1
    )

    print("Published:", message)

    time.sleep(3)