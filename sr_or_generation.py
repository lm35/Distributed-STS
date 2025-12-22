
#To read invalid occupants alone
import csv
from modules import config
# Re-import necessary libraries after execution state reset
import pandas as pd
import numpy as np


def stateoccupancy_gen(file_validinvalid_occup, file_staterelation, reduced_SR_output_path, OR_Estimated_path, inputfile_SR_GT_path, OR_GT_path, occupant_IDs_path,zone_IDs_path):
    # Define the CSV file path
    #file_validinvalid_occup = config.ESTIMATED_VALIDTRACK  # Update with actual file path

    #Path to Full State Relation
    #file_staterelation = config.WHOLE_STATE_RELATION_ESTIMATED
    #Path to reduced state relation
    #reduced_SR_output_path = config.REDUCED_STATE_RELATION_ESTIMATED
    #Path to occupancy relation file
    #OR_Estimated_path = config.OCCUPANCY_ESTIMATED
    #Ground Truth SR
    #inputfile_SR_GT_path = config.SR_GT_CSTS
    #Path to GT OR
    #OR_GT_path = config.WHOLE_OR_GT
    with open(occupant_IDs_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0 # To check if all rows are being read
        namLablDict = {}
        nameList = []
        nameidList = []
        for row in csv_reader:
            namLablDict.update({row["Occupant Name"]:row["OccupID"]})
            nameList.append(row["Occupant Name"])
            nameidList.append(row["OccupID"])
            line_count += 1
        occupcount = len(nameidList)
    with open(zone_IDs_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0 # To check if all rows are being read
        zone_Dict = {}
        zoneList = []
        for row in csv_reader:
            zone_Dict.update({row["zone"]:row["id"]})
            zoneList.append(row["zone"])
            line_count += 1
        zonecount = len(zoneList)
        print("Zonelist",zoneList)


    repeat_factor = occupcount * zonecount #To repeat the number of time stamps for 'ToTime'
    header_staterelation = ["Time","OccupantID","Zone","Probability"]
    with open(reduced_SR_output_path, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header_staterelation)  # Writing column headers


    header_occupancyrelation = ["FromTime","ToTime","OccupantID","Zone","Probability"]
    with open(OR_Estimated_path, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header_occupancyrelation)  # Writing column headers
    #Write headers into Ground Truth OR file
    with open(OR_GT_path, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header_occupancyrelation)  # Writing column headers
#===================================================Reduced State Relation Estimated============================================

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_validinvalid_occup)

    # Filter occupants with 'Invalid' TrackStatus
    invalid_tracks_df = df[df["TrackStatus"] == "Invalid"][["EstimatedOccupantID"]]

    # Convert to a list (if needed for further processing)
    invalid_tracks_list = invalid_tracks_df["EstimatedOccupantID"].tolist()
    print(invalid_tracks_list)
    # Display the DataFrame with invalid occupants
    #import ace_tools as tools
    #tools.display_dataframe_to_user(name="Invalid Tracks", dataframe=invalid_tracks_df)

    # Print the list for reference
    print("[INFO] List of occupants with invalid tracks:", invalid_tracks_list)
    len_invalidoccup = len(invalid_tracks_list)
    new_repeatfactor = repeat_factor - (len_invalidoccup*zonecount)
    print("Repeat Factor", repeat_factor)
    #Reading full state relation
    df_state = pd.read_csv(file_staterelation)

    # Ensure the "OccupantID" column exists before filtering
    if "OccupantID" in df_state.columns:
        # Filter rows where "OccupantID" is NOT in invalid_tracks_list
        filtered_df = df_state[~df_state["OccupantID"].isin(invalid_tracks_list)]

        # Save the filtered DataFrame to a new CSV file with the same header
        filtered_df.to_csv(reduced_SR_output_path, index=False)

        print(f"[INFO] Filtered data saved to '{reduced_SR_output_path}'")
    else:
        print("[ERROR] 'OccupantID' column not found in the CSV file.")

#===========================================================Occupancy relation Ground Truth#======================================================
    #Occuancy relation for Ground Truth
    df_occupancy_gt = pd.read_csv(inputfile_SR_GT_path)
    print("df_occupancy is",df_occupancy_gt)
    time_counts_gt = df_occupancy_gt["Time"].value_counts().reset_index()
    print("ount is",time_counts_gt)
    # Get unique sorted time values
    unique_times_gt = df_occupancy_gt["Time"].unique()#Get the unique timestamps from the list
    timestamps_gt = unique_times_gt[1:] # Remove the first time stap
    print("Legth is greater and displayed again", len(timestamps_gt), repeat_factor)
    for i in timestamps_gt:
        print("Each time stamp is",i)
    print("unique_time",timestamps_gt)
    sort_timestamps_gt = sorted(timestamps_gt)
    # Check if all counts are the same
    if len(timestamps_gt) == 1:
        common_count_gt = timestamps_gt[0]
        print(f"All counts are the same: {common_count_gt}")
    else:
        print("Count mismatch")
    # Repeat each timestamp No. of occuants * Zonecount times
    repeat_factor = occupcount * zonecount
    enlarged_list_gt = np.repeat(timestamps_gt, repeat_factor)
    if (len(timestamps_gt)< len(unique_times_gt)):
        print("Legth is greater difference is ", len(timestamps_gt)-len(unique_times_gt), len(timestamps_gt), repeat_factor)
        last_element_gt = np.repeat(timestamps_gt[-1],repeat_factor)
        enlarged_list_gt = np.append(enlarged_list_gt, last_element_gt)
    print("Enlarged list",enlarged_list_gt)
    print("Lenght of enlarged list", len(enlarged_list_gt))
    print("Legth is greater and displayed again", len(timestamps_gt), repeat_factor)

    # Convert to a DataFrame
    df_occupancy_gt["ToTime"] = pd.DataFrame({"ToTime": enlarged_list_gt})
    print("to_time is",df_occupancy_gt["ToTime"])
    print("Lenght f final totime is", len(df_occupancy_gt["ToTime"]))
    print("Lenght f final Fomtime is", len(df_occupancy_gt["Time"]))

    df_occupancy_gt = df_occupancy_gt[["Time","ToTime","OccupantID","Zone","Probability"]]
    # Rename the column "Time" to "FromTime"
    df_occupancy_gt.rename(columns={"Time": "FromTime"}, inplace=True)
    # Save the occupancy relation data to a new CSV file
    df_occupancy_gt.to_csv(OR_GT_path, index=False)
#================================================#Occuancy relation estimated#============================================================
    #new_repeatfactor is used as the invalid occupant state information needs to be removed
    # Read the reduced state relation CSV
    df_occupancy = pd.read_csv(reduced_SR_output_path)
    print("df_occupancy is",df_occupancy)
    time_counts = df_occupancy["Time"].value_counts().reset_index()
    print("Count is",time_counts)
    # Get unique sorted time values
    unique_times = df_occupancy["Time"].unique()#Get the unique timestamps from the list
    timestamps = unique_times[1:] # Remove the first time stap
    print("unique_time",timestamps)
    # Check if all counts are the same
    if len(timestamps) == 1:
        common_count = timestamps[0]
        print(f"All counts are the same: {common_count}")
    else:
        print("Count mismatch")
    # Repeat each timestamp 270 times
    enlarged_list = np.repeat(timestamps, new_repeatfactor)
    if len(timestamps) < len(unique_times):
        print("GT Length difference is",len(timestamps)-len(unique_times))
        last_element = np.repeat(timestamps[-1],new_repeatfactor)
        enlarged_list = np.append(enlarged_list, last_element)
    print("Enlarged GT list",enlarged_list)
    print("Estmated GT Lenght of enlarged list", len(enlarged_list_gt))
    print("Estimated GT Legth is greater and displayed again", len(timestamps_gt), repeat_factor)

    # Convert to a DataFrame
    df_occupancy["ToTime"] = pd.DataFrame({"ToTime": enlarged_list})
    print("to_time GT is",df_occupancy["ToTime"])
    df_occupancy = df_occupancy[["Time","ToTime","OccupantID","Zone","Probability"]]
    # Rename the column "Time" to "FromTime"
    df_occupancy.rename(columns={"Time": "FromTime"}, inplace=True)
    # Save the occupancy relation data to a new CSV file
    df_occupancy.to_csv(OR_Estimated_path, index=False)
    print("New repeat factorGT is ",new_repeatfactor)
