import random
import pandas as pd
import datetime
import itertools
import csv
import os
import pickle
import config
from collections import Counter
from random import randrange

def read_occupant_ids(file_path):
    df = pd.read_csv(file_path)
    return df["occupID"].tolist()

def gen_occup_GTtrack(scriptDict_start, scriptDict, scriptDict_end, count_building):
    """Generates a ground truth track for occupants."""
    full_track = []
    for _ in range(3):  # Iterate 3 times to extend the track length
        track = scriptDict_start["entrance"][:]  # Start with entrance
        track.extend(random.choice(scriptDict[random.choice(list(scriptDict.keys()))]))  # Intermediate activity
        track.extend(scriptDict_end["exit"])  # End with exit
        random_number = random.randint(1, count_building)
        full_track.extend([f"{zone}_{random_number}" for zone in track])
    return full_track

def generate_unique_timestamps(track, full_timestamp):
    """Generates unique timestamps for each event in a track."""
    unique_time_stamps = set(full_timestamp)  # Keep track of existing timestamps
    sorted_timestamps = []
    today_date = datetime.datetime.today().strftime("%Y-%m-%d")
    start_time = datetime.datetime.strptime("07:00:00", "%H:%M:%S")
    end_time = datetime.datetime.strptime("20:00:00", "%H:%M:%S")
    total_seconds = (end_time - start_time).seconds

    for _ in range(len(track)):
        while True:
            new_timestamp = (start_time + datetime.timedelta(seconds=random.randint(0, total_seconds))).strftime("%Y-%m-%d %H:%M:%S")
            if new_timestamp not in unique_time_stamps:
                unique_time_stamps.add(new_timestamp)
                sorted_timestamps.append(new_timestamp)
                break
            else:
                # If duplicate, increment by 1 second
                start_time += datetime.timedelta(seconds=1)

    # Sort timestamps to maintain chronological order
    sorted_timestamps.sort(key=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    return sorted_timestamps

def generate_ground_tracks():
    """Generates and writes the ground truth occupant tracks."""
    # Read occupant IDs
    file_path = config.OCCUPANT_IDS_INIT
    df = pd.read_csv(file_path)
    occupant_ids = df["OccupID"].tolist()
    occupant_names = df["Occupant Name"].tolist()

    # Create output directory
    output_dir = "groundtruth_tracks"
    os.makedirs(output_dir, exist_ok=True)

    scriptDict_start = {"entrance": ["entrance"]}
    scriptDict_end = {"exit": ["exit", "transit"]}
    scriptDict = {
        "teach_3": [["mailroom", "entrance", "classroom"], ["lounge", "entrance", "classroom"]],
        "goto_office_3": [["mailroom", "lounge", "office"], ["lounge", "mailroom", "office"]],
        "lunch_break_3": [["lounge", "entrance", "cafeteria"], ["mailroom", "entrance", "cafeteria"]],
        "meeting_3": [["lounge", "office", "conf_room"], ["lounge", "mailroom", "conf_room"]]
    }

    # Read building IDs
    file_path = config.BUILDING_IDS
    df = pd.read_csv(file_path)
    count_building = len(df["BuildingID"].tolist())

    full_timestamp = set()  # Store all timestamps for uniqueness check
    one_day_event = []

    # Limit occupants for testing
    num_occupants = min(100, len(occupant_ids))
    selected_occupant_ids = occupant_ids[:num_occupants]
    selected_occupant_names = occupant_names[:num_occupants]

    # Generate tracks
    for occupant_id, occupant_name in zip(selected_occupant_ids, selected_occupant_names):
        track = gen_occup_GTtrack(scriptDict_start, scriptDict, scriptDict_end, count_building)
        time_stamp = generate_unique_timestamps(track, full_timestamp)
        full_timestamp.update(time_stamp)

        for i in zip(time_stamp, track, itertools.repeat(occupant_id, len(track))):
            one_day_event.append(list(i))

    # Sort events by timestamp
    sorted_event_list = sorted(one_day_event, key=lambda x: datetime.datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S"))

    # Assign unique event IDs (e1, e2, e3, ...)
    for idx, event in enumerate(sorted_event_list, start=1):
        event.insert(0, f"e{idx}")

    # Write to main CSV
    csv_filename = os.path.join(output_dir, "mixedTrack.csv")
    with open(csv_filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Event", "Time", "Zone", "GT"])
        csvwriter.writerows(sorted_event_list)

    print(f"Sorted event list saved to {csv_filename}")

    # Write zone-wise CSVs
    zone_files = {}
    for event in sorted_event_list:
        zone_index = event[2].split('_')[-1]  # Extract last part of the zone
        filename = os.path.join(output_dir, f"OccupVisitTrack_b{zone_index}.csv")
        zone_files.setdefault(filename, []).append(event)

    for filename, data in zone_files.items():
        with open(filename, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Event", "Time", "Zone", "GT"])
            csvwriter.writerows(data)
        print(f"Data saved to {filename}")
