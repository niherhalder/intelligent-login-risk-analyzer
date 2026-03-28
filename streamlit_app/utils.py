import pandas as pd
from sklearn.ensemble import IsolationForest


def classify_risk(score: int) -> str:
    if score >= 6:
        return "High"
    elif score >= 3:
        return "Medium"
    return "Low"


def train_model(feature_path: str = "outputs/processed_features.csv"):
    X = pd.read_csv(feature_path)

    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )
    model.fit(X)

    return model, X.columns.tolist()


def prepare_login_features(
    user: str,
    time_str: str,
    location: str,
    device_or_browser: str,
    status: str,
    training_columns: list[str]
):
    login_time = pd.to_datetime(time_str, format="%H:%M")
    hour = login_time.hour

    is_failed = 1 if status.lower() == "failed" else 0
    is_night_login = 1 if 0 <= hour <= 5 else 0
    is_high_risk_location = 1 if location == "Russia" else 0
    is_suspicious_device = 1 if device_or_browser == "Mobile" else 0

    feature_dict = {
        "is_failed": is_failed,
        "is_night_login": is_night_login,
        "is_high_risk_location": is_high_risk_location,
        "is_suspicious_device": is_suspicious_device
    }

    for col in training_columns:
        if col not in feature_dict:
            feature_dict[col] = 0

    user_col = f"user_{user}"
    location_col = f"location_{location}"
    device_col = f"device_or_browser_{device_or_browser}"

    if user_col in feature_dict:
        feature_dict[user_col] = 1
    if location_col in feature_dict:
        feature_dict[location_col] = 1
    if device_col in feature_dict:
        feature_dict[device_col] = 1

    feature_df = pd.DataFrame([feature_dict])
    feature_df = feature_df[training_columns]

    return feature_df, hour


def detect_login_risk(
    user: str,
    time_str: str,
    location: str,
    device_or_browser: str,
    status: str,
    model,
    training_columns: list[str]
):
    feature_df, hour = prepare_login_features(
        user=user,
        time_str=time_str,
        location=location,
        device_or_browser=device_or_browser,
        status=status,
        training_columns=training_columns
    )

    risk_score = (
        feature_df["is_failed"].iloc[0] * 3 +
        feature_df["is_night_login"].iloc[0] * 2 +
        feature_df["is_high_risk_location"].iloc[0] * 3 +
        feature_df["is_suspicious_device"].iloc[0] * 1
    )

    risk_level = classify_risk(risk_score)
        # Build explainable risk factors
    risk_factors = []

    if feature_df["is_failed"].iloc[0] == 1:
        risk_factors.append("Failed login attempt")

    if feature_df["is_night_login"].iloc[0] == 1:
        risk_factors.append("Night-time login")

    if feature_df["is_high_risk_location"].iloc[0] == 1:
        risk_factors.append("High-risk location")

    if feature_df["is_suspicious_device"].iloc[0] == 1:
        risk_factors.append("Suspicious device usage")

    prediction = model.predict(feature_df)[0]
    model_anomaly_label = "Anomaly" if prediction == -1 else "Normal"

    # Final system decision: high rule-based risk OR model anomaly
    if risk_level == "High" or model_anomaly_label == "Anomaly":
        final_decision = "Anomaly"
    else:
        final_decision = "Normal"

    alert = final_decision == "Anomaly"

    return {
        "user": user,
        "time": time_str,
        "hour": hour,
        "location": location,
        "device_or_browser": device_or_browser,
        "status": status,
        "risk_score": int(risk_score),
        "risk_level": risk_level,
        "model_anomaly_label": model_anomaly_label,
        "final_decision": final_decision,
        "alert": alert,
        "risk_factors": risk_factors
    }