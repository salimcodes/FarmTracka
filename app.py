# Step 1: Data Preparation
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset from Excel file
data = pd.read_excel("data.xlsx")

# Handle missing values if any
data.dropna(inplace=True)


# Split data into features and target
X = data.iloc[:, :-1]  # Features (light intensity, temperature, humidity)
y = data.iloc[:, -1]   # Target (plant growth status)

# Encode target variable into numbers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Model Training with XGBoost
import xgboost as xgb

# Initialize the model
model = xgb.XGBClassifier()

# Train the model
model.fit(X, y_encoded)

# Step 4: Streamlit App Development
import streamlit as st
import replicate
import os

def run_arctic_instruct(prompt, temperature, replicate_api_token):
  """Fetches response from Snowflake Arctic Instruct using Replicate API"""
  try:
    # Get API token from environment variable (replace with your actual variable name)
    replicate_api_token = replicate_api_token
    if not replicate_api_token:
      st.error("SNOWFLAKE ARTIC INSTRUCT API TOKEN NOT SET!")
      return

    input_data = {
      "prompt": prompt,
      "temperature": temperature
    }

    # Use replicate.stream for live output with progress bar
    for event in replicate.stream(
      "snowflake/snowflake-arctic-instruct",
      input=input_data
    ):
      yield str(event)

  except Exception as e:
    st.error(f"An error occurred: {e}")


# Define the Streamlit app
def main():
    st.title("AgriTracka")
    st.subheader("Your Farm's Digital Guardian")
    st.markdown("""
        Welcome to AgriTracka! Please input the light intensity, temperature, and humidity levels of your farm's environment. 
       Provide your Snowflake Arctic Instruct API key to get personalized advice for maintaining your plant.
        """)    
    # Input fields for user
    light_intensity = st.number_input("Light Intensity (in lux)", min_value=0, max_value=15000, step=1, help="Enter the current light intensity in lux.")
    temperature = st.number_input("Temperature (in °C)", min_value=0, max_value=50, step=1, help="Enter the current temperature in degrees Celsius.")
    humidity = st.number_input("Humidity (in %)", min_value=0, max_value=100, step=1, help="Enter the current humidity percentage.")
    api_key = st.text_input("Enter API Key", type="password", help="Enter your API key to get advice.")


    # Ensure inputs are valid
    if st.button('Predict Plant Status and Advice the Farmer'):
        if not api_key:
            st.error("Please enter a valid API key.")
        else:
          try:
            prediction = model.predict([[light_intensity, temperature, humidity]])
            # Decode the predicted label
            predicted_status = label_encoder.inverse_transform(prediction)
            # Display prediction
            predicted_status = predicted_status[0]
            st.write("Predicted Plant Status:", predicted_status)
        
            prompt_text = "As an agriculturist, give advice to an African farmer on how to deal with a " + predicted_status + " plant."
            temperature = 0.8
            response = run_arctic_instruct(prompt_text, temperature, api_key)
            full_response = st.write_stream(response)
          except Exception as e:
                st.error(f"An error occurred: {e}")


# Run the app
if __name__ == "__main__":
    main()

