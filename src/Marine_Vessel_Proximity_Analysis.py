import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load the data into a pandas DataFrame
df = pd.read_csv('sample_data.csv')

# Define the Haversine Formula
def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))

    # Radius of Earth in kilometers
    r = 6371.0
    return c * r

# Create a key column for Cartesian product
df['key'] = 1

# Perform a Cartesian product
df_pairs = df.merge(df, on='key', suffixes=('_1', '_2'))

# Remove self-pairs (where a vessel is paired with itself)
df_pairs = df_pairs[df_pairs['mmsi_1'] != df_pairs['mmsi_2']]

# Calculate distances in a vectorized manner
df_pairs['distance'] = haversine(
    df_pairs['lat_1'], df_pairs['lon_1'],
    df_pairs['lat_2'], df_pairs['lon_2']
)

# Set the proximity threshold in kilometers
proximity_threshold = 1.0

# Filter pairs that are within the proximity threshold
close_proximity_df = df_pairs[df_pairs['distance'] <= proximity_threshold]

# Create a scatter plot for vessel positions
fig = px.scatter(df, x='lon', y='lat', color='mmsi', title='Marine Vessel Positions')

# Add lines for vessels in close proximity
for _, row in close_proximity_df.iterrows():
    fig.add_trace(go.Scattergeo(
        lon=[row['lon_1'], row['lon_2']],
        lat=[row['lat_1'], row['lat_2']],
        mode='lines',
        line=dict(color='red', width=2),
        showlegend=False
    ))

# Update layout for better visualization
fig.update_layout(
    geo=dict(
        projection_type="equirectangular",
        showland=True,
        landcolor="rgb(217, 217, 217)",
        subunitcolor="rgb(255, 255, 255)",
        countrycolor="rgb(255, 255, 255)"
    ),
    title={
        'text': "Vessel Positions and Proximity Events",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

# Show the plot
fig.show()
