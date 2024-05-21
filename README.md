# FarmTracka: Your Farm's Digital Guardian


Up to 40% of farmers in Nigeria lose their crops due to preventable factors. FarmTracka is an intelligent web application designed to help farmers monitor the health of their plants based on environmental conditions such as light intensity, temperature, and humidity. Using machine learning and AI-powered advice, FarmTracka provides predictions on plant status and offers AI-enabled personalized advice to maintain plant health.

## Table of Contents

- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
- [Streamlit App Development](#streamlit-app-development)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Hardware](#hardware)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Installation

Before you begin, ensure you have Python 3.7+ installed. Follow these steps to set up the environment and install the necessary packages:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/farmtracka.git
    cd farmtracka
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Data Preparation

To prepare the data for training, follow these steps:

1. Load the dataset from an Excel file using pandas.
2. Handle any missing values by dropping or imputing them.
3. Split the data into features (light intensity, temperature, humidity) and the target (plant growth status).
4. Encode the target variable using `LabelEncoder` from scikit-learn.

## Model Training

The model underneath was trained using the RandomForest classifier:

1. Initialize the RandomForest Classifier model.
2. Train the model on the prepared dataset.

## Streamlit App Development

Develop the Streamlit app to interact with the model and get advice:

1. Set up the Streamlit app structure.
2. Create input fields for light intensity, temperature, humidity, and API key.
3. Implement the prediction logic to display the predicted plant status.
4. Fetch advice using the Snowflake Arctic Instruct API and display it in the app.

## Running the Application

To run the application, use the following command:

```bash
streamlit run app.py
```

This command starts the Streamlit server and opens the app in your default web browser.

## Hardware

- For Humidity:
  
![image](https://github.com/salimcodes/FarmTracka/assets/64667212/f5470969-325a-4fd3-9f38-570224d363db)

- For Light Intensity:

![image](https://github.com/salimcodes/FarmTracka/assets/64667212/499b8f39-d562-4586-a197-91a4d2dc44fc)

- For Temperature:

  ![image](https://github.com/salimcodes/FarmTracka/assets/64667212/1a052236-00e5-4558-9cfd-6f42eaac4613)


## Usage

1. Open the Streamlit app in your web browser.
2. Enter the light intensity, temperature, and humidity levels.
3. Provide your Snowflake Arctic Instruct API key.
4. Click the 'Predict Plant Status and Advice the Farmer' button to get the plant status and personalized advice.

## Acknowledgements

- The machine learning model was trained using the RandomForest Classifier.
- The app fetches advice using the Snowflake Arctic Instruct via the Replicate API.
- Special thanks to the open-source community for providing the tools and resources used in this project.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for more details.


## This is the hardware part of the solution!

#### Description
FarmTracka is an application designed for agricultural monitoring and management. It utilizes two hardware components: a light intensity sensor - a Photoresistor (a LDR - Light Dependent Resistor) and a DHT11 sensor (i.e. Digital Humidity and Temperature Sensor) for temperature and humidity sensing. These sensors are interfaced with an Arduino microcontroller to collect environmental data, which is then displayed on an LCD screen. The project consists of two main components: `sensing.ino` for data collection and `actuating.ino` for displaying sensor values on the LCD screen.

---

#### Folder Structure

- **sensing**:
  - **sensing.ino**: Arduino code for collecting data from sensors and sending it to the serial monitor and then exported to a spreadsheet using Coolterm, a freeware serial port terminal app and networking program.

- **actuating**:
  - **actuating.ino**: Arduino code for displaying sensor data on the LCD screen.

---

#### Hardware Requirements
- Arduino Uno Microcontroller
- DHT11 Temperature and Humidity Sensor
- Light Intensity Sensor- Photoresistor i.e. a LDR - Light Dependent Resistor
- LCD Screen
- Resistors, wires, and breadboard (for circuit connection)

---

#### Setup Instructions
1. Connect the DHT11 Temperature and Humidity Sensor to the designated pin on the Arduino board.
2. Connect the Light Intensity Sensor to the analog pin of the Arduino board.
3. Wire the LCD screen according to the pin configurations specified in the code (`rs`, `en`, `d4`, `d5`, `d6`, `d7`).
4. Upload the `sensing.ino` code to the Arduino board to read sensor data.
5. Upload the `actuating.ino` code to the Arduino board to display sensor data on the LCD screen.

---

#### Operation
1. Upon powering the Arduino board, the `sensing.ino` code starts collecting data from the sensors.
2. The temperature, humidity, and light intensity readings are displayed on the serial monitor.
3. Simultaneously, the `actuating.ino` code displays the sensor data on the connected LCD screen.
4. The data is updated at regular intervals, providing real-time environmental information.

