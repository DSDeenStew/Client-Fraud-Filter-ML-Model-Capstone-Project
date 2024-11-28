import streamlit as st
import numpy as np
import pickle
import pandas as pd

# @st.cache_data
df = pd.read_csv('cleaned_fraud_data.csv')


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model_loaded = data["model"]
le_country = data["le_country"]
le_prov_state = data["le_prov_state"]
le_gender = data["le_gender"]
le_age_group = data["le_age_group"]
le_fraud_cat = data["le_fraud_cat"]
le_solic_method = data["le_solic_method"]
scaler_loaded = data["scaler"]


def show_predict_page():
    st.title('Client Fraud Predictor Tool')
    st.write("""###### The following tool classifies a clients online report of Cybercrime or Fraudulent activity performed against them as Fraudulent or not.""")
    st.write("""###### The prediction tool predicts to  the accuracy of 83% and is formed off The Canadian Anti-Fraud Reporting Data from 2021-2024.""")

    st.write("""### Please provide the following client information:""")

    country = st.selectbox("Client residing Country", options=df['Country'].unique())
    province = st.selectbox("Client residing Province/State", options=sorted(df['Major Province/State'].unique()))
    gender = st.selectbox("Client Gender", options=df['Gender'].unique())
    age = st.selectbox("Client Age Group", options=df['Victim Age Group'].unique())

    st.write("""### Please categorize the client complaint among the following:""")

    fraud_type = st.selectbox("Type of Fraud or Cybercrime", options=df['Fraud/Cybercrime Category'].unique())
    solic = st.selectbox("Method of Solicitation", options=df['Solicitation Method'].unique())
    

    ok = st.button("Predict")
    if ok:
        X_input = np.array([[country, province, gender, age, fraud_type, solic ]])
        X_input[:, 0] = le_country.transform(X_input[:,0])
        X_input[:, 1] = le_prov_state.transform(X_input[:,1])
        X_input[:, 2] = le_gender.transform(X_input[:,2])
        X_input[:, 3] = le_age_group.transform(X_input[:,3])
        X_input[:, 4] = le_fraud_cat.transform(X_input[:,4])
        X_input[:, 5] = le_solic_method.transform(X_input[:,5])

        X_input = X_input.astype(float)
        scaled_X_input = scaler_loaded.transform(X_input)



        prediction = model_loaded.predict(scaled_X_input)

        if prediction[0] == 1:
            st.subheader("YES! The client has most likely been a victim of FRAUD.")
        else:
            st.subheader("NO! The client is most likely NOT a victim of fraud.")