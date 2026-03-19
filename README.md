# # 🎓 Student Career & Job Predictor (SVM) – Streamlit App

## 📌 Overview
A Machine Learning web application built with **Streamlit** that predicts whether a student has a **part-time job** using a Support Vector Machine (SVM) classifier.

The model is dynamically trained inside the app using student academic and behavioral features.


The application provides:
* Loads student dataset
* Performs preprocessing (encoding + scaling)
* Splits data into training and testing sets
* Trains an SVM classifier
* Displays model accuracy
* Allows manual prediction for a single student

---

##  🛠 Tech Stack

* Python 3.9+
* Streamlit
* Pandas
* Scikit-learn
* NumPy

  
⚠️ Important:
Update the dataset path inside `app.py` before deployment. Currently it uses:
```python
f = pd.read_csv(r"c:\Users\Lenovo\Downloads\Student_Placement_Career_Prediction_Dataset.csv")
```

## 📊 Features Used for Prediction

The model uses the following numerical features:

* absence_days
* weekly_self_study_hours
* math_score
* history_score
* physics_score
* chemistry_score
* biology_score
* english_score
* geography_score

Target Variable:

```
part_time_job
```
---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Cleaning

* Gender column capitalized
* Label Encoding applied to target

### 2️⃣ Train-Test Split

* Adjustable test size (10%–50%)
* Controlled using Streamlit slider

### 3️⃣ Feature Scaling

* StandardScaler used
* Applied before SVM training

### 4️⃣ Model Training

* Algorithm: XGBoosting
* Kernel selectable from:


### 🤖 ML Prediction
- Custom input-based prediction
- Trained model (`best_model.pkl`)
- Real-time prediction output

---

### 5️⃣ Evaluation

* Accuracy Score displayed in UI

---

### UI Sections

✔ Dataset Preview
✔ Model Accuracy Display
✔ Kernel Selection
✔ Adjustable Test Size
✔ Manual Student Prediction Tool

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/student-job-svm.git
cd student-job-svm
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## ☁️ Streamlit Cloud Deployment

1. Push project to GitHub
2. Go to Streamlit Cloud
3. Select repository
4. Choose `app.py`
5. Deploy

Ensure:

* `student-scores.csv` is inside repository
* File path in `app.py` is relative
* All dependencies listed in `requirements.txt`

---

## 📦 Example requirements.txt

```
streamlit
pandas
scikit-learn
numpy
```

---

## 🧠 Model Explanation

This app uses ** XGBoost (eXtreme Gradient Boosting)**:

* Sequential Learning: Builds decision trees sequentially, where each new tree corrects errors (residuals) of previous trees.
* Gradient Boosting: Uses gradient descent to minimize the loss function while adding new models to the ensemble.
* Regularization: Applies L1/L2 regularization to prevent overfitting and improve model generalization.
* Sparsity-Awareness: Natively handles missing values by learning the best split direction during training. 

---

## ⚠️ Limitations

* Model retrains every time app runs
* No hyperparameter tuning
* Only accuracy metric used
* No confusion matrix or precision/recall

---

## 👨‍💻 Author

Fardeen khan
Machine Learning & Data Science Enthusiast
Skilled in Python, SQL, ML Deployment & Analytics

---
## 📁 Project Structure

```text
Student_placement_prediction-streamlit-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── df = Student_Placement_Career_Prediction_Dataset
.csv
│
├── model/
│   └── best_model.pkl
│
└── notebooks/
    └── Student_Placement_prediction
```
