# AI-Powered Infrastructure Failure Prediction using Machine Learning

This project presents a **low-cost AI-powered Structural Health Monitoring (SHM) system** that detects early signs of infrastructure failures using multi-sensor data and deep learning models.

The system combines **IoT sensor nodes, edge computing, and machine learning** to continuously monitor buildings, bridges, and industrial structures and detect anomalies before critical failure occurs.

---

# Project Overview

Modern infrastructure such as buildings, bridges, and industrial assets experience continuous stress from environmental and operational loads. Unexpected failures can lead to **safety hazards, economic losses, and operational downtime**.

This project proposes an **AI-based predictive monitoring system** capable of analyzing real-time sensor data and detecting structural anomalies using deep learning. The system classifies structural conditions as:

- Healthy
- Minor Damage
- Severe Damage

The solution enables **early damage detection and predictive maintenance for infrastructure systems.**

---

# Key Features

- Multi-sensor structural monitoring system
- Real-time anomaly detection
- Edge AI deployment on ESP32
- Deep learning-based damage prediction
- Low-cost scalable sensor network
- Distributed SHM nodes with anomaly voting
- Real-time infrastructure health monitoring

---

# System Architecture

The system consists of three main components:

1. **IoT Sensor Node**
   - ESP32 microcontroller
   - Accelerometer
   - Strain gauge
   - Temperature sensor

2. **Machine Learning Model**
   - 1D CNN Encoder
   - CNN Decoder
   - Autoencoder-based anomaly detection

3. **Edge Deployment**
   - Model optimized using TensorFlow Lite
   - Runs directly on ESP32 device for real-time inference

---

# Methodology

The workflow of the system includes:

1. **Sensor Data Acquisition**
   - Collect time-series data from accelerometer, strain gauge, and temperature sensors.

2. **Data Preprocessing**
   - Noise filtering
   - Signal normalization
   - Window segmentation of sensor signals.

3. **Feature Extraction**
   - Time-series features are extracted using a **1D CNN Encoder**.

4. **Model Training**
   - Pretrained CNN encoder on large SHM datasets.
   - Fine-tuned decoder for structure-specific behavior.

5. **Anomaly Detection**
   - Reconstruction error is calculated.
   - If error exceeds threshold → anomaly detected.

6. **Damage Classification**
   - Healthy
   - Minor Damage
   - Severe Damage

---

# Hardware Components

| Component | Description |
|--------|--------|
| ESP32 | Edge microcontroller |
| ADXL345 Accelerometer | Vibration monitoring |
| Strain Gauge | Structural stress measurement |
| DS18B20 Sensor | Temperature monitoring |
| HX711 Amplifier | Signal amplification |
| LiPo Battery | Portable power supply |

Estimated cost per sensor node: **₹2405**

---

# Software & Tools

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- MATLAB
- Google Colab
- Streamlit Dashboard

---

# Machine Learning Model

The project uses a **Hybrid CNN Autoencoder architecture**.

### Encoder
Extracts vibration and structural patterns from time-series data.

### Decoder
Reconstructs input signals and calculates reconstruction error.

### Anomaly Detection
Structural damage is detected based on reconstruction error thresholds.

---

# Model Performance

- Accuracy: **94%**
- Final F1 Score: **0.94**
- ROC AUC: **0.988**

---

# Applications

This system can be deployed in:

- Smart buildings
- Bridges
- Industrial plants
- Towers
- Infrastructure monitoring systems

---

# Future Improvements

- LoRaWAN communication for long-range IoT deployment
- Higher precision industrial sensors
- Distributed mesh network monitoring
- Real-time cloud dashboards
- Self-learning anomaly detection models

---


