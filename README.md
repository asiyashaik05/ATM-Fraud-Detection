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

# Run the app:
* python app.py



# 🗂️ Project Structure
Code

ATM-Fraud-Detection/

├── app.py

├── README.md

├── confusion_matrix.png

├── precision_recall_curve.png

├── roc_curve.png

└── final_output.png


# ⚠️ Limitations
* Detection depends on predefined fraud patterns and trained ML models. Unknown fraud tactics may not be recognized.

* Large transaction datasets may slow down analysis on limited hardware.

* Fraud detection scores are approximate and may not perfectly reflect real-world fraud.

* Currently supports only English-language transaction logs.

* Cloud deployment (Streamlit Cloud) may have file size limits for uploaded datasets.

* Does not automatically integrate with live banking systems — analysis is per uploaded dataset.


# 🖼️ App Preview

 <img width="500" height="400" alt="confusion_matrix" src="https://github.com/user-attachments/assets/055c62ee-d2b0-47c3-8e35-6da409d6b2ad" />
<img width="640" height="480" alt="precision_recall_curve" src="https://github.com/user-attachments/assets/5d843aed-1ffc-4108-b64e-465005d9cbd5" />
<img width="640" height="480" alt="roc_curve" src="https://github.com/user-attachments/assets/47f4e9b4-d03a-443f-bbc9-e64ceff7d0f2" />
<img width="1920" height="1080" alt="final_output" src="https://github.com/user-attachments/assets/b7fc3642-9c90-417b-a4f3-259a50699771" />


# ⚖️ License
This project is open-source and free to use
