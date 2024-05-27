import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2
import plotly.express as px
import plotly.graph_objects as go

# Read the CSV file into a DataFrame
df = pd.read_csv('sample_data.csv')

# Display the DataFrame to understand its structure
print(df)

# Step 2: Implement the algorithm to identify vessel proximity events
def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Earth radius in kilometers
    return distance

def find_vessel_proximity(df, threshold_distance):
    # Initialize an empty dictionary to store vessel proximity events
    vessel_proximity = {}

    # Group DataFrame by timestamp
    grouped = df.groupby('timestamp')

    # Iterate over groups
    for timestamp, group in grouped:
        # Initialize a list to store vessels in proximity
        proximity_list = []
        
        # Iterate over each vessel's position
        for i in range(len(group)):
            current_mmsi = group.iloc[i]['mmsi']
            current_lat = group.iloc[i]['lat']
            current_lon = group.iloc[i]['lon']
            
            # Check proximity with other vessels in the group
            for j in range(i + 1, len(group)):
                other_mmsi = group.iloc[j]['mmsi']
                other_lat = group.iloc[j]['lat']
                other_lon = group.iloc[j]['lon']
                
                distance = haversine_distance(current_lat, current_lon, other_lat, other_lon)
                if distance <= threshold_distance:
                    proximity_list.append((current_mmsi, other_mmsi))
        
        # Add to the dictionary
        vessel_proximity[timestamp] = proximity_list
    
    return vessel_proximity

# Set the threshold distance in kilometers
threshold_distance = 1

# Find vessel proximity events
proximity_events = find_vessel_proximity(df, threshold_distance)

# Step 3: Create a final DataFrame with the required columns
final_df = pd.DataFrame(columns=['timestamp', 'vessel1', 'vessel2'])

# Create an empty list to store DataFrame rows
rows = []

# Iterate over proximity events and add them to the final DataFrame
for timestamp, proximity_list in proximity_events.items():
    for vessel1, vessel2 in proximity_list:
        rows.append({'timestamp': timestamp, 'vessel1': vessel1, 'vessel2': vessel2})

# Concatenate the list of rows into a DataFrame
final_df = pd.concat([final_df, pd.DataFrame(rows)], ignore_index=True)

print(final_df.head(10))

# Step 4: Visualize the results using Plotly

# Count the number of proximity events per timestamp
event_counts = final_df['timestamp'].value_counts().reset_index()
event_counts.columns = ['timestamp', 'event_count']

# Create a time series plot of proximity events
fig = px.line(event_counts, x='timestamp', y='event_count', title='Number of Vessel Proximity Events Over Time')
fig.update_layout(xaxis_title='Timestamp', yaxis_title='Number of Proximity Events')
fig.show()

# Create a scatter plot of vessel pairs in proximity
fig = px.scatter(final_df, x='vessel1', y='vessel2', color='timestamp', title='Vessel Proximity Events',
                 labels={'vessel1': 'Vessel 1 MMSI', 'vessel2': 'Vessel 2 MMSI'})
fig.update_layout(xaxis_title='Vessel 1 MMSI', yaxis_title='Vessel 2 MMSI')
fig.show()
