# P311 — IoT-Based Fault Diagnosis System

An IoT-based system for monitoring machine sensor data, detecting abnormal operating conditions, and visualizing machine health in real time.

## Overview

P311 collects simulated industrial sensor readings, processes them through an MQTT pipeline, identifies potential machine faults, and stores the results for monitoring and analysis.

## Key Features

- **Sensor simulation:** Generates temperature, vibration, and current readings.
- **MQTT communication:** Transfers sensor data through HiveMQ Cloud.
- **Fault detection:** Identifies abnormal readings and classifies machine status.
- **Database storage:** Stores sensor readings, timestamps, and detected faults in SQLite.
- **REST API:** Provides endpoints for latest readings and historical data.
- **Dashboard visualization:** Uses Grafana to display sensor trends and machine status.
- **Containerization:** Uses Docker and Docker Compose for deployment.

## Architecture

```text
Sensor Simulator
       |
       v
   HiveMQ Cloud
       |
       v
   MQTT Receiver
       |
       v
 Fault Detection
       |
       v
   SQLite Database
       |
       +------> Flask REST API
       |
       +------> Grafana Dashboard
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Messaging | MQTT, HiveMQ Cloud |
| Backend | Flask, Flask-CORS |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Visualization | Grafana |
| Deployment | Docker, Docker Compose |

## Project Structure

```text
P311-IoT-Fault-Diagnosis/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── fault_detector.py
│   └── mqtt_receiver.py
├── data/
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── simulator/
│   └── sensor_simulator.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or compatible version
- Docker Desktop
- HiveMQ Cloud account and MQTT credentials
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/riyanshi-ji/P311-IoT-Fault-Diagnosis.git
   cd P311-IoT-Fault-Diagnosis
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your HiveMQ Cloud connection using a local configuration file or environment variables. **Do not commit passwords or credentials.**

### Run the Application

Start the backend API and Grafana services:

```bash
docker compose up --build -d
```

Run the sensor simulator and MQTT receiver in separate terminals, using your configured environment:

```bash
python -m simulator.sensor_simulator
```

```bash
python -m backend.mqtt_receiver
```

Open the services:

- **Flask API:** http://localhost:5000
- **Grafana:** http://localhost:3000

The simulator and MQTT receiver require valid broker configuration. Configure the Grafana SQLite data source and dashboard as needed for your environment.

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | API home or health response |
| `/api/latest` | Latest sensor reading |
| `/api/history` | Historical sensor readings |

## Future Improvements

- Add predictive maintenance using machine learning.
- Introduce configurable fault thresholds.
- Add alerts for critical machine conditions.
- Expand monitoring to multiple machines.
- Improve automated deployment and testing.

## Author

**Riyanshi Jain**  
B.Tech — Computer Science and Engineering  
ABES Engineering College

## License

See the repository's selected license, if one is included.
