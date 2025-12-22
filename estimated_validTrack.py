import pandas as pd
#from modules
from modules import config


def gen_validTrack(input_csv_path,output_csv_path):
    try:

        # Define the input and output CSV file paths
        #input_csv_path = config.ESTIMATED_OCCUPANTS  # Update this with your actual file path
        #output_csv_path = config.ESTIMATED_VALIDTRACK

        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_csv_path)
        if df.empty:
            print(f"[WARNING] Input file '{input_csv_path}' is empty. Skipping processing.")
            empty_df = pd.DataFrame(columns=["EstimatedOccupantID", "AverageProbability", "TrackStatus"])
            empty_df.to_csv(output_csv_path, index=False)
            return

        # Group by 'EstimatedOccupant' and compute the average probability
        df_avg = df.groupby("EstimatedOccupantID", as_index=False)["Probability"].mean()

        # Add 'TrackStatus' column based on the average probability
        df_avg["TrackStatus"] = df_avg["Probability"].apply(lambda x: "Valid" if x >= 0.90 else "Invalid")

        # Rename columns to match the required output format
        df_avg.rename(columns={"Probability": "AverageProbability"}, inplace=True)

        # Write the processed data to a new CSV file
        df_avg.to_csv(output_csv_path, index=False)

        # Print confirmation
        print(f"[INFO] Processed occupant data saved to: {output_csv_path}")
    except pd.errors.EmptyDataError:
        print(f"[ERROR] Input file '{input_csv_path}' is completely empty (no header).")
        # Also write an empty file with headers
        empty_df = pd.DataFrame(columns=["EstimatedOccupantID", "AverageProbability", "TrackStatus"])
        empty_df.to_csv(output_csv_path, index=False)
    except FileNotFoundError:
        print(f"[ERROR] Input file '{input_csv_path}' not found.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
