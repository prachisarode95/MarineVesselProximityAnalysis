
# Marine Vessel Proximity Analysis

This assignment project demonstrates how to calculate marine vessel proximity events using Python libraries such as Pandas, Numpy, and Math. It utilizes the Haversine formula. It also showcases the Pandas vectorization method and visualizes the final result using Plotly.

## Project Structure

- **data/sample_data.csv**: Contains the Vessel locations, Vessel IDs, and Timestamp data.
- **src/Marine_Vessel_Proximity_Analysis.py and Marine_Vessel_Proximity_Analysis.ipynb**: Python scripts to run the analysis.
- **README.md**: Assignment documentation.
- **requirements.txt**: Python dependencies.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-username>/<repository-name>.git
    cd <repository-name>
    ```

2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the analysis script:

    ```bash
    python src/Marine_Vessel_Proximity_Analysis.py
    ```


# We'll explore the code to identify vessel proximity events and visualize the results.

## Libraries Used
1. **pandas (pd)**:
   - Used for reading CSV files and handling structured data.

2. **numpy (np)**:
   - Used for performing mathematical operations.

3. **math (radians, sin, cos, sqrt, atan2)**:
   - Used for calculating distances using the haversine formula.

4. **plotly.express (px)**:
   - Used for creating scatter and line plots.

5. **plotly.graph_objects (go)**:
   - Used for enhancing plot customization.

## Code Explanation

1. **Importing Libraries:**
   Started with importing Pandas for data handling, NumPy & Math for mathematical operations, and Plotly for visualizations.

2. **Reading Data:**
   Read the data from the 'sample_data.csv' file into a pandas DataFrame to understand its structure.

3. **Haversine Distance Function:**
   Defined the `haversine_distance` function to calculate the haversine distance, which is the shortest distance over the Earth's surface between two points, given their latitude and longitude.

4. **Finding Vessel Proximity Events:**
   Defined the `find_vessel_proximity` function to identify the pairs of vessels that are within a specified distance of each other. It groups the data by timestamp and calculates the distance between each pair of vessels.

5. **Setting Threshold Distance:**
   Set a threshold distance of 1 kilometer to identify proximity events.

6. **Creating Proximity Events DataFrame:**
   Stored the proximity events in a DataFrame, which includes the timestamps and pairs of vessels that were close to each other.

7. **Visualizing Results:**
   Created two plots using Plotly. The first plot shows the number of proximity events over time, and the second plot displays the pairs of vessels that were in proximity.

## Plot Explanation

**Time Series Plot:**
This plot shows the number of vessel proximity events over time. The x-axis represents the timestamp, and the y-axis represents the number of proximity events. It helps us see trends and patterns in vessel interactions over time.

**Scatter Plot:**
This plot displays pairs of vessels that were in proximity. Each point represents a pair of vessels that were within the threshold distance of each other. The color indicates the timestamp, helping us understand when these events occurred.

**Conclusion:**
This code reads the vessel data, identifies proximity events using the haversine formula, and visualizes these events to help analyze marine traffic patterns. This approach is crucial for understanding vessel interactions and potential collision risks.

## Final Results

![Number of Marine Vessel Proximity Events Over Time](https://github.com/prachisarode95/MarineVesselProximityAnalysis/assets/60979131/ead775a2-1192-4645-9a9d-51023d9c59ba)

![Marine Vessel Proximity Events](https://github.com/prachisarode95/MarineVesselProximityAnalysis/assets/60979131/77b3109f-b5cc-4ece-8062-da11137881c8)

