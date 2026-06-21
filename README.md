# heart-disease-prediction
it is a classification machine learning model use to predict the high or low level of heart disease  through  best classification model
# ❤️ Heart Disease Prediction using KNN and Streamlit

## 📌 Project Overview

This project is a Machine Learning-based Heart Disease Prediction System developed using Python, Scikit-Learn, and Streamlit. The application predicts whether a person is at high risk or low risk of heart disease based on medical parameters entered by the user.

The model is trained using the K-Nearest Neighbors (KNN) algorithm and deployed through an interactive Streamlit web application.

---

## 🚀 Features

* User-friendly Streamlit interface
* Real-time heart disease prediction
* Data preprocessing using feature scaling
* Machine Learning model trained with KNN
* Supports categorical and numerical medical attributes
* Instant risk assessment

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* Joblib

---

## 📊 Input Parameters

The model uses the following patient information:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol Level
* Fasting Blood Sugar
* Maximum Heart Rate
* Exercise-Induced Angina
* Resting ECG Results
* Oldpeak (ST Depression)

---

## 🧠 Machine Learning Model

Algorithm Used:

* K-Nearest Neighbors (KNN)

Preprocessing:

* Feature Encoding
* Feature Scaling using StandardScaler

Model Files:

* `knn_heart.pkl`
* `scaler.pkl`
* `columns.pkl`

---

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── main.py
├── knn_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run main.py
```

---

## 📈 Workflow

1. User enters medical information.
2. Data is converted into a structured format.
3. Features are scaled using the saved scaler.
4. KNN model predicts the risk level.
5. Result is displayed instantly on the web interface.

---

## 🎯 Future Improvements

* Add more machine learning algorithms for comparison.
* Improve prediction accuracy through hyperparameter tuning.
* Deploy the application on Streamlit Cloud.
* Add data visualization dashboards.
* Include probability/confidence scores.

---

## 👨‍💻 Author

Ashutosh Joshi

Computer Science Student | Machine Learning Enthusiast | AI Developer

---

## ⭐ Support

If you found this project useful, please consider giving it a star on GitHub.
