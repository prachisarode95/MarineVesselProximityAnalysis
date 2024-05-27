import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

def haversine(lon1, lat1, lon2, lat2):
    R = 6371.0  # Earth radius in kilometers
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c
    return distance

def find_proximity_events(data, threshold_distance):
    coordinates = data[['lat', 'lon']].values
    mmsis = data['mmsi'].values
    timestamps = data['timestamp'].values
    tree = cKDTree(coordinates)
    threshold_distance_radians = threshold_distance / 6371.0
    pairs = tree.query_pairs(threshold_distance_radians)
    proximity_events = []
    for i, j in pairs:
        if mmsis[i] != mmsis[j]:
            proximity_events.append({
                'mmsi': mmsis[i],
                'vessel_proximity': mmsis[j],
                'timestamp': timestamps[i]
            })
            proximity_events.append({
                'mmsi': mmsis[j],
                'vessel_proximity': mmsis[i],
                'timestamp': timestamps[j]
            })
    return pd.DataFrame(proximity_events)

data = pd.read_csv('sample_data.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])
threshold_distance = 5.0
proximity_events = find_proximity_events(data, threshold_distance)

output_df = proximity_events.groupby('mmsi').agg({
    'vessel_proximity': list,
    'timestamp': 'first'
}).reset_index()

# Visualization
fig = px.scatter(data, x='lon', y='lat', color='mmsi', hover_data=['mmsi', 'timestamp'])

for _, row in proximity_events.iterrows():
    vessel_1 = data[data['mmsi'] == row['mmsi']].iloc[0]
    vessel_2 = data[data['mmsi'] == row['vessel_proximity']].iloc[0]
    fig.add_trace(go.Scattergeo(
        lon=[vessel_1['lon'], vessel_2['lon']],
        lat=[vessel_1['lat'], vessel_2['lat']],
        mode='lines',
        line=dict(width=1, color='red'),
        opacity=0.5
    ))

fig.update_layout(
    title='Marine Vessel Proximity Events',
    showlegend=False,
    geo=dict(
        scope='world',
        projection_type='equirectangular',
        showland=True,
    )
)

fig.show()
