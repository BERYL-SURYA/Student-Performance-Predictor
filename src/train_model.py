import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("data/student_performance.csv")

# Remove Student_ID
df = df.drop("Student_ID", axis=1)

# Encode Stress_Level
encoder = LabelEncoder()
df["Stress_Level"] = encoder.fit_transform(df["Stress_Level"])

# Features and Target
X = df.drop("GPA", axis=1)
y = df["GPA"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Train Model
# -------------------------------
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -------------------------------
# Predictions
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------
print("\n========== MODEL PERFORMANCE ==========\n")

print("R2 Score :", round(r2_score(y_test, y_pred), 3))
print("MAE      :", round(mean_absolute_error(y_test, y_pred), 3))
print("RMSE     :", round(mean_squared_error(y_test, y_pred) ** 0.5, 3))

# -------------------------------
# Save Model
# -------------------------------
joblib.dump(model, "model/student_model.pkl")
joblib.dump(encoder, "model/label_encoder.pkl")

print("\n✅ Model Saved Successfully!")