# FarmTracka: Your Farm's Digital Guardian

FarmTracka is an intelligent web application designed to help farmers monitor the health of their plants based on environmental conditions such as light intensity, temperature, and humidity. Using machine learning and AI-powered advice, FarmTracka provides predictions on plant status and offers AI-enabled personalized advice to maintain plant health.

## Table of Contents

- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
- [Streamlit App Development](#streamlit-app-development)
- [Running the Application](#running-the-application)
- [Usage](#usage)
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
