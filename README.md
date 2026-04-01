# ATM Fraud Detection AI v5.7

An AI-powered Streamlit app that detects and analyzes suspicious ATM transactions to provide:

 * ✅ Real-time fraud risk score
   
* 💡 Smart AI alerts & recommendations

* 🧭 Transaction anomaly detection

* 📊 PDF analysis report


# ✨ Features

* Upload transaction datasets (CSV, XLSX, JSON, TXT)

* Paste or stream live transaction logs

* AI analyzes transaction patterns, flags anomalies, and provides fraud risk scores

* Generates a PDF report of suspicious activity

* Suggests preventive measures and compliance checks

* Supports hybrid detection (rule-based + ML-based)

# Install dependencies:
* pip install -r requirements.txt

# Run the Streamlit app:
* streamlit run app.py



# 🗂️ Project Structure
Code

ATM-Fraud-Detection/

├── app.py

├── requirements.txt

├── README.md

├── dashboard.png

├── alerts.png

├── anomalies.png

└── report.png


# ⚠️ Limitations
* Detection depends on predefined fraud patterns and trained ML models. Unknown fraud tactics may not be recognized.

* Large transaction datasets may slow down analysis on limited hardware.

* Fraud detection scores are approximate and may not perfectly reflect real-world fraud.

* Currently supports only English-language transaction logs.

* Cloud deployment (Streamlit Cloud) may have file size limits for uploaded datasets.

* Does not automatically integrate with live banking systems — analysis is per uploaded dataset.


# 🖼️ App Preview












# ⚖️ License
This project is open-source and free to use
