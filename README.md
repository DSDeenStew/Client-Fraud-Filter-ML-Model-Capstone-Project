# Client-Fraud-Filter-ML-Model-Capstone-Project
by: Naudeen Stewart

[Presentation Link](https://docs.google.com/presentation/d/1p9GwR3LYV8EQ2CV3NEqhBMEyduPsoPbzAjV_YSgRTCs/edit?usp=sharing)



This Project will produce a machine learning model capable of classifying a client’s Complaint Report of Fraudulent activity as a Victim of Fraud or Not. This Fraud Predictor Tool aims to aide financial institutions and busineses by being able to filter the predicted outcome of such reports based on the likelihood of the client to be a Victim of Fraud or Not, therefore seperating cases to be handled accordingly with better insight and by coordinated personel.

### Data:
- The project is built off the analysis the Canadian Anti-Fraud Centre Fraud Reporting System Dataset obtained from [Open Canada](https://open.canada.ca/data/en/dataset/6a09c998-cddb-4a22-beff-4dca67ab892f) 
- The [Original Dataset](fraud_dataset.zip) is contained in a CSV file in a compressed folder.
- Exploratory Data Analysis is performed in the [Fraud Data Notebook](fraud_data.ipynb)
- The [Cleaned Data Frame](cleaned_fraud_data.csv) is saved into a CSV file in order to use for model building.

### Model Building:
- All steps are performed in the [Fraud Model Building Notebook](Fraud_Model_Building.ipynb).
- The Final model utilizes Random Forest Classifier and has an overall accuracy of 83%.
- All encoders, scalar and model are saved into the following [pickle file](saved_steps.pkl)

### Streamlit App
The application created allows a user to both use The Predictor Tool and Exlplore an Overview of the Data Analysis.
It is deployed to the cloud and can be found at the following link [Streamlit Fraud Filter App](https://fraud-app-final-project-6vewjensft3r7dquozkbps.streamlit.app/).
The Tool predicts an outcome based on the following categorical features from the Data:
- Country
- Major City/Province
- Gender
- Age Group
- Fraud/Cybercrime Category
- Solicitation Method

*VS code Files:*
- [Main Page](fraud_filter_app.py)
- [Predict Page](predict_page.py)
- [Explore Page](explore_page.py)


