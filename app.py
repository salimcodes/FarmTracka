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


from sklearn.linear_model import LogisticRegression

# Initialize the Logistic Regression classifier
model = LogisticRegression(max_iter=200, random_state=42)

# Train the model
model.fit(X, y_encoded)

# Step 4: Streamlit App Development
import streamlit as st
import replicate
import os

def run_arctic_instruct(prompt, temperature):
  """Fetches response from Snowflake Arctic Instruct using Replicate API"""
  try:
    # Get API token from environment variable 
    replicate_api_token = os.environ.get("REPLICATE_API_TOKEN")
    if not replicate_api_token:
      st.error("REPLICATE_API_TOKEN environment variable not set!")
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
    st.title("Plant Status Predictor")
    
    # Input fields for user
    light_intensity = st.number_input("Light Intensity", min_value=0, max_value=15000, step=1)
    temperature = st.number_input("Temperature", min_value=0, max_value=50, step=1)
    humidity = st.number_input("Humidity", min_value=0, max_value=100, step=1)
    

    # Make prediction
    if st.button('Predict Plant Status and Advice the Farmer'):
        prediction = model.predict([[light_intensity, temperature, humidity]])
        # Decode the predicted label
        predicted_status = label_encoder.inverse_transform(prediction)
        # Display prediction
        predicted_status = predicted_status[0]
        st.write("Predicted Plant Status:", predicted_status)
    
        prompt_text = "As an agriculturist, give advice to an African farmer on how to deal with a " + predicted_status + " plant."
        temperature = 0.8
        response = run_arctic_instruct(prompt_text, temperature)
        full_response = st.write_stream(response)


# Run the app
if __name__ == "__main__":
    main()

