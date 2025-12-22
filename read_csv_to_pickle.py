import csv
import pickle

# Define file paths
csv_file_path = "random_indexperFullGT.csv"  # Replace with your actual CSV file
pickle_file_path = "data.pkl"  # Output pickle file

# Read CSV into a dictionary
data_dict = {}

with open(csv_file_path, mode="r") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        if len(row) < 2:
            continue  # Skip empty or invalid rows

        name = row[0]  # First column is the key (actor name)

        # Convert list of numbers from string format to integers
        numbers = [int(num.strip(" []")) for num in row[1:]]  # Strip brackets & spaces

        # Store in dictionary
        data_dict[name] = numbers

# Save dictionary to pickle
with open(pickle_file_path, "wb") as pickle_file:
    pickle.dump(data_dict, pickle_file)

print(f"CSV data has been saved as a pickle file: {pickle_file_path}")

# ---- Now, Read the Pickle File and Display Its Content ----
with open(pickle_file_path, "rb") as pickle_file:
    loaded_data = pickle.load(pickle_file)

print("\n[INFO] Content of the Pickle File:")
print(loaded_data)  # Print as dictionary
