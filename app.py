import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, precision_recall_curve
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# 1. Generate synthetic ATM transaction dataset
# -----------------------------
np.random.seed(42)
n_samples = 1000
fraud_ratio = 0.05  # 5% fraud

amounts = np.random.randint(50, 20000, n_samples)
times = np.random.randint(0, 24, n_samples)
locations = np.random.choice(['NewYork', 'London', 'Paris'], n_samples)

# Fraud labels: mostly 0, with ~5% 1
is_fraud = np.zeros(n_samples)
fraud_indices = np.random.choice(n_samples, int(n_samples*fraud_ratio), replace=False)
is_fraud[fraud_indices] = 1

df = pd.DataFrame({
    'transaction_id': range(1, n_samples+1),
    'amount': amounts,
    'time': times,
    'location': locations,
    'is_fraud': is_fraud.astype(int)
})

# -----------------------------
# 2. Extra engineered features
# -----------------------------
df['high_amount'] = (df['amount'] > 5000).astype(int)
df['night_transaction'] = df['time'].apply(lambda x: 1 if (x >= 22 or x <= 5) else 0)
df['amount_per_time'] = df['amount'] / (df['time'] + 1)
df['is_weekend'] = df['time'].apply(lambda x: 1 if x in [0,6,12,18,23] else 0)
df['amount_category'] = pd.cut(df['amount'], bins=[0,1000,10000,20000], labels=[0,1,2]).astype(int)
location_risk_map = {'NewYork':0, 'London':1, 'Paris':2}
df['location_risk'] = df['location'].map(location_risk_map)
df['suspicious_pattern'] = ((df['high_amount']==1) & (df['night_transaction']==1)).astype(int)

df.to_csv("atm_transactions_large.csv", index=False)
print("✅ Synthetic dataset created: atm_transactions_large.csv with", n_samples, "rows")

# -----------------------------
# 3. Load dataset
# -----------------------------
data = pd.read_csv("atm_transactions_large.csv")

# -----------------------------
# 4. Feature Engineering
# -----------------------------
data = data.drop(columns=['transaction_id'])
data = pd.get_dummies(data, columns=['location'], drop_first=True)

X = data.drop('is_fraud', axis=1)
y = data['is_fraud']

# -----------------------------
# 5. Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# -----------------------------
# 6. Scale Features
# -----------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 7. Train Model
# -----------------------------
model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# -----------------------------
# 8. Evaluate Model
# -----------------------------
y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("ROC-AUC:", roc_auc_score(y_test, model.predict_proba(X_test)[:,1]))

# Confusion Matrix plot
plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.show()

# ROC curve plot
fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label="ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.savefig("roc_curve.png")
plt.show()

# Precision-Recall curve plot
precision, recall, _ = precision_recall_curve(y_test, model.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(recall, precision, label="Precision-Recall Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.savefig("precision_recall_curve.png")
plt.show()

# -----------------------------
# 9. Anomaly Detection (Isolation Forest)
# -----------------------------
iso = IsolationForest(contamination=fraud_ratio, random_state=42)
iso.fit(X_train)
anomaly_scores = iso.predict(X_test)
print("\nIsolation Forest anomaly predictions (first 10):", anomaly_scores[:10])

# -----------------------------
# 10. Example Prediction
# -----------------------------
new_transaction = pd.DataFrame({
    'amount': [15000],
    'time': [2],
    'location': ['Paris'],
    'high_amount': [1],
    'night_transaction': [1],
    'amount_per_time': [15000/3],
    'is_weekend': [0],
    'amount_category': [2],
    'location_risk': [2],
    'suspicious_pattern': [1]
})

new_transaction = pd.get_dummies(new_transaction)
new_transaction = new_transaction.reindex(columns=X.columns, fill_value=0)

new_transaction_scaled = scaler.transform(new_transaction)
prediction = model.predict(new_transaction_scaled)
print("\nFraud Prediction:", "Fraud" if prediction[0] == 1 else "Legit")





