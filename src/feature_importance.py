import joblib
import matplotlib.pyplot as plt

# Load Model
model = joblib.load("model/student_model.pkl")

# Feature Names
features = [
    "Study Hours",
    "Extra Curricular",
    "Sleep",
    "Social",
    "Physical Activity",
    "Stress Level"
]

importance = model.feature_importances_

plt.figure(figsize=(8,5))
plt.bar(features, importance)

plt.title("Feature Importance")

plt.xlabel("Features")
plt.ylabel("Importance")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("screenshots/feature_importance.png")

plt.show()