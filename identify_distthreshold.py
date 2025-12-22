import pandas as pd

# Load the CSV file
file_path = "b10_distanceThreshold.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand structure
df.head()


# Rename columns for clarity
df.columns = ["DistanceThreshold", "OccupantID", "ActualClass", "PredictedClass", "IsCorrect"]

# Convert IsCorrect to boolean if needed
df["IsCorrect"] = df["IsCorrect"].astype(bool)

# Group by DistanceThreshold and calculate correct/wrong counts
result = df.groupby("DistanceThreshold")["IsCorrect"].agg([
    ("CorrectPredictions", lambda x: (x == True).sum()),
    ("WrongPredictions", lambda x: (x == False).sum())
]).reset_index()

result.to_csv("b10_prediction_accuracy_by_threshold.csv", index=False)
print("Saved results to prediction_accuracy_by_threshold.csv")
