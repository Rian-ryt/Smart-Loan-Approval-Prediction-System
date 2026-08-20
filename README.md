# Smart Loan Approval Prediction System

## 📌 Overview

The **Smart Loan Approval Prediction System** is a machine learning-based application that predicts whether a loan application is likely to be **approved or rejected** based on applicant and loan-related information.

The project uses machine learning algorithms to analyze loan application data and generate predictions through a web-based interface.

## 🎯 Objective

The main objective of this project is to develop an intelligent loan approval prediction system using machine learning techniques.

The system demonstrates how machine learning can be applied to a real-world financial decision-making problem by analyzing applicant information and predicting loan approval outcomes.

## ✨ Features

* Predicts loan approval based on applicant and loan-related details
* Uses multiple machine learning algorithms
* Performs data preprocessing and feature scaling
* Provides a web-based user interface
* Generates loan approval predictions
* Includes trained machine learning models
* Includes a Jupyter Notebook for model development and experimentation
* Contains separate frontend and backend components
* Includes a loan approval dataset for model development

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning & Data Processing

* Pandas
* NumPy
* Scikit-learn

### Web Technologies

* HTML
* CSS

### Development Tools

* Jupyter Notebook
* Visual Studio Code

## 🤖 Machine Learning Models

The project uses multiple machine learning algorithms for loan approval prediction:

* **Logistic Regression**
* **Decision Tree**
* **Random Forest**
* **Support Vector Machine (SVM)**

These models are used to explore and compare different approaches for predicting loan approval outcomes.

## 🔄 Project Workflow

```text
Loan Application Data
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Feature Scaling
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Trained Model
        ↓
User Input
        ↓
Loan Approval Prediction
```

## 📁 Project Structure

```text
Smart-Loan-Approval-Prediction-System/
│
├── backend/
│   ├── app.py
│   ├── model.pkl
│   └── scaler.pkl
│
├── datasets/
│   └── loan_approval_dataset.csv
│
├── frontend/
│   └── index.html
│
├── Loan_Pred_System.ipynb
│
├── package.json
├── package-lock.json
├── .gitignore
└── README.md
```

## 📊 Dataset

The project uses a loan approval dataset containing applicant and loan-related information.

The dataset is used for:

* Data preprocessing
* Exploratory analysis
* Feature preparation
* Machine learning model training
* Model evaluation
* Loan approval prediction

## 🧠 Model Files

The trained machine learning components are stored in the backend:

* `model.pkl` — trained machine learning model
* `scaler.pkl` — feature scaling object

These files are used by the application to generate predictions from user-provided loan information.

## 💻 Frontend

The frontend is implemented using **HTML and CSS**.

The interface allows users to enter the required loan application information and interact with the prediction system.

The frontend code is located in:

```text
frontend/index.html
```

## ⚙️ Backend

The backend contains the application logic required to process user input and generate loan approval predictions.

The backend code is located in:

```text
backend/app.py
```

The trained model and scaler are also stored inside the backend directory.

## 📓 Jupyter Notebook

The project includes the Jupyter Notebook:

```text
Loan_Pred_System.ipynb
```

The notebook contains the machine learning development process, including data analysis, preprocessing, model training, and experimentation.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Rian-ryt/Smart-Loan-Approval-Prediction-System.git
```

### 2. Open the project

```bash
cd Smart-Loan-Approval-Prediction-System
```

### 3. Install the required Python libraries

Make sure Python is installed on your system and install the libraries used by the project:

```bash
pip install pandas numpy scikit-learn
```

### 4. Run the backend application

```bash
python backend/app.py
```

> The exact command may vary depending on how the backend application is configured.

### 5. Open the frontend

Open:

```text
frontend/index.html
```

in a web browser and use the application interface.

## 📌 Future Enhancements

* Improve model prediction accuracy
* Add additional machine learning models
* Improve the user interface and user experience
* Add real-time model performance monitoring
* Deploy the application online
* Add user authentication
* Add detailed prediction explanations
* Add visualization of loan application data

## 👩‍💻 Author

**Rianna Kristin M.**

B.Tech – Artificial Intelligence and Data Science

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

**Smart Loan Approval Prediction System**
*Machine Learning for Smarter Loan Decision Support*
