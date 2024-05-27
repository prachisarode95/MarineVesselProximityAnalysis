
# Marine Vessel Proximity Analysis

This project shows the calculataion on marine vessel proximity using Python and analyzes vessel proximity events using the Haversine formula and Pandas vectorization and visualize them using data visualization libraries.

## Project Structure

## Libraries Used
- Pandas
- Numpy
- Plotly

## Methodology Used
- Haversine formula : to calculate distances between two individual vessels.
- Pandas vectorization - To faster the data processing time.


- **data/vessel_positions.csv**: Contains the vessel position data.
- **src/vessel_proximity_analysis.py**: Main Python script for the analysis.
- **README.md**: Project documentation.
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
    python src/vessel_proximity_analysis.py
    ```

## Explanation of the Code

1. **Import Libraries**:
    - `pandas`: For data manipulation.
    - `numpy`: For numerical operations.
    - `plotly`: For interactive visualization.

2. **Load Data**:
    - Load vessel positions from `sample_data.csv`.

3. **Haversine Formula**:
    - Calculate distances between geographic coordinates using the Haversine formula.

4. **Calculate Pairwise Distances**:
    - Generate all possible pairs of vessel positions and calculate distances between them.

5. **Filter Proximity Events**:
    - Identify vessel pairs within the specified proximity threshold.

6. **Visualization**:
    - Visualize vessel positions and highlight proximity events using Plotly.

## Data
- Ensure your data file (`sample_data.csv`) is in the `data` directory.
- The CSV file should contain the following columns: `mmsi`, `timestamp`, `lat`, `lon`.




