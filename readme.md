IPL Win Predictor

Project Mentored By: Surekha Kanwar

Project Overview

The IPL Win Predictor is a machine learning–based application that predicts the win probability of an IPL cricket match based on the current match situation. The prediction dynamically updates using real-time match parameters such as runs, wickets, and overs remaining.

This project demonstrates an end-to-end data science workflow including data analysis, feature engineering, model training, and deployment using Streamlit.

Project Structure

IPL_Win_Predictor.ipynb
Jupyter Notebook used for data exploration, preprocessing, feature engineering, and model training.

app.py
Streamlit web application that provides an interactive user interface for win probability prediction.

matches.csv
Dataset containing IPL match-level information.

deliveries.csv
Ball-by-ball delivery dataset used for feature generation.

pipe.pkl
Trained machine learning pipeline generated from the notebook.

requirements.txt
List of required Python dependencies.

Procfile & setup.sh
Deployment configuration files (used for platforms such as Heroku).

How to Run the Project

Install Dependencies

pip install -r requirements.txt


Train the Model

Open and run the IPL_Win_Predictor.ipynb notebook.

This will train the model and generate the pipe.pkl file.

Run the Application

streamlit run app.py

Model Details

Algorithm Used: Logistic Regression

Target: Predict win probability of the batting team

Key Features:

Runs left

Balls left

Wickets left

Current Run Rate (CRR)

Required Run Rate (RRR)

The trained model outputs a probability score representing the likelihood of the batting team winning the match based on the current match state.

Note

This repository is maintained for student project submissions and learning purposes, where students showcase their end-to-end machine learning and deployment work under mentorship.
