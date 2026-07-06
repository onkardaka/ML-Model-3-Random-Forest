# E-Commerce Fraud Detection System (Random Forest)

Welcome! This is an intelligent real-time fraud detection system for e-commerce transactions. The project features a predictive machine learning model trained in **Google Colab** using the **Random Forest** algorithm, deployed as an interactive web application via **Streamlit**.

**Try the live web app here!** -> [👉 Link to my Streamlit App 👈](https://model-3-random-forest.streamlit.app/)

---

##  Project Features

The model evaluates multiple transaction variables instantly to calculate the risk score of fraud.

###  The ML Core
* **Algorithm:** `RandomForestClassifier` optimized for swift production environments.
* **Analyzed Features:** Transaction amount, customer age, quantity of products, hour of the day, payment method, product category, device used, and a custom feature engineering variable (`Amount per Age`).
* **Optimization:** The model has been compressed and fine-tuned in depth (`max_depth=12`, `n_estimators=50`) to guarantee an ultra-fast prediction response (< 0.01s) and a lightweight repository footprint (< 25 MB).

---

## Repository Structure

* `app.py`: The main script for the interactive web user interface built with Streamlit.
* `modelo_fraude_random_forest.joblib`: The pre-trained production-ready model binary.
* `requirements.txt`: Configuration file containing required dependencies (`streamlit`, `scikit-learn`, `pandas`, `joblib`).

---

## 🛠️ Local Installation and Usage

To replicate and run this project on your local machine, open your terminal and follow these steps:

1. **Clone the repository or download the source files.**
2. **Install the required dependencies:**
   ```bash
   python -m pip install -r requirements.txt
